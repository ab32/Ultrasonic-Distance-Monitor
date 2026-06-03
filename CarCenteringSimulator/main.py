import tkinter as tk


class CarCenteringSimulator:

    def __init__(self, root):

        self.root = root

        self.root.title("Wash Hall Centering Simulator")

        self.canvas_width = 1000
        self.canvas_height = 600

        self.canvas = tk.Canvas(
            root,
            width=self.canvas_width,
            height=self.canvas_height,
            bg="white"
        )

        self.canvas.pack()

        self.left_wall = 100
        self.right_wall = 900

        self.car_width = 200
        self.car_height = 100

        self.car_x = 400
        self.car_y = 220

        self.draw_static_objects()

        self.car = self.canvas.create_rectangle(
            self.car_x,
            self.car_y,
            self.car_x + self.car_width,
            self.car_y + self.car_height,
            fill="lightblue"
        )

        self.sensor_text = self.canvas.create_text(
            500,
            40,
            text="",
            font=("Arial", 16)
        )

        self.status_text = self.canvas.create_text(
            500,
            70,
            text="",
            font=("Arial", 16, "bold")
        )

        self.gauge_line = self.canvas.create_line(
            250,
            500,
            750,
            500,
            width=4
        )

        self.canvas.create_text(
            250,
            530,
            text="LEFT"
        )

        self.canvas.create_text(
            750,
            530,
            text="RIGHT"
        )

        self.canvas.create_text(
            500,
            530,
            text="CENTER"
        )

        self.needle = self.canvas.create_line(
            500,
            430,
            500,
            500,
            width=6
        )

        self.canvas.tag_bind(
            self.car,
            "<B1-Motion>",
            self.drag_car
        )

        self.update_display()

    def draw_static_objects(self):

        self.canvas.create_rectangle(
            self.left_wall,
            100,
            self.left_wall + 20,
            400,
            fill="gray"
        )

        self.canvas.create_rectangle(
            self.right_wall - 20,
            100,
            self.right_wall,
            400,
            fill="gray"
        )

        self.canvas.create_text(
            self.left_wall,
            80,
            text="LEFT SENSOR"
        )

        self.canvas.create_text(
            self.right_wall,
            80,
            text="RIGHT SENSOR"
        )

    def drag_car(self, event):

        new_x = event.x - (self.car_width / 2)

        if new_x < self.left_wall + 25:
            new_x = self.left_wall + 25

        if new_x > self.right_wall - self.car_width - 25:
            new_x = self.right_wall - self.car_width - 25

        self.car_x = new_x

        self.canvas.coords(
            self.car,
            self.car_x,
            self.car_y,
            self.car_x + self.car_width,
            self.car_y + self.car_height
        )

        self.update_display()

    def update_display(self):

        left_distance = int(
            self.car_x - self.left_wall
        )

        right_distance = int(
            self.right_wall -
            (self.car_x + self.car_width)
        )

        offset = right_distance - left_distance

        self.canvas.itemconfig(
            self.sensor_text,
            text=(
                f"Left Sensor: {left_distance} mm    "
                f"Right Sensor: {right_distance} mm"
            )
        )

        if abs(offset) < 20:

            status = "CENTERED"

        elif offset > 0:

            status = "MOVE RIGHT"

        else:

            status = "MOVE LEFT"

        self.canvas.itemconfig(
            self.status_text,
            text=(
                f"Offset: {offset} mm    {status}"
            )
        )

        gauge_center = 500

        needle_x = gauge_center + (offset * 0.5)

        if needle_x < 250:
            needle_x = 250

        if needle_x > 750:
            needle_x = 750

        self.canvas.coords(
            self.needle,
            needle_x,
            430,
            needle_x,
            500
        )


root = tk.Tk()

app = CarCenteringSimulator(root)

root.mainloop()