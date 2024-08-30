import flet as ft

class App:
    def __init__(self, page: ft.Page):
        self.page = page
        self.page.title = 'Galeria de Fotos'
        self.page.padding = 0
        self.page.window_title_bar_hidden = False
        self.page.window_height = 750
        self.page.window_width = 500
        self.page.window_resizable = False
        self.main()
    
    def main(self):
        
        def change_view(e):
            all_button.bgcolor = ft.colors.GREY_500
            all_button.color = ft.colors.BLACK
            all_button.update()
            filter_button.bgcolor = ft.colors.GREY_500
            filter_button.color = ft.colors.BLACK
            filter_button.update()
            e.control.bgcolor = ft.colors.GREY_900
            e.control.color = ft.colors.WHITE
            e.control.update()

            # filter_button.update()
            # all_button.update()

            if e.control.text == 'Agrupadas':
                layout.content.controls[0] = photo_grid_2
            else:
                layout.content.controls[0] = photo_grid_1
            layout.update()

        def image(num: int):
            return ft.Image(
                src = f'https://picsum.photos/150/150?{num}',
                fit = ft.ImageFit.COVER,
                repeat = ft.ImageRepeat.NO_REPEAT,
            ) 
        
        all_button = ft.ElevatedButton(
            text = 'Todas as fotos',
            bgcolor = ft.colors.GREY_900,
            color = ft.colors.WHITE,
            elevation = 0,
            col = 6,
            on_click = change_view,
        )

        filter_button = ft.ElevatedButton(
            text = 'Agrupadas',
            bgcolor = ft.colors.GREY_500,
            color = ft.colors.BLACK,
            elevation = 0,
            col = 6,
            on_click = change_view,
        )

        photo_grid_1 = ft.GridView(
            controls = [image(num = num) for num in range(100)],
            runs_count = 5,
            spacing = 5,
            run_spacing = 5,
            expand = True,
            child_aspect_ratio = 1.0,
        )

        photo_grid_2 = ft.Column(
            expand = True,
            controls = [
                ft.Text(value = '2022', size = 30),
                ft.GridView(
                    controls = [image(num = num) for num in range(1, 40)],
                    runs_count = 5,
                    spacing = 5,
                    run_spacing = 5,
                    expand = True,
                    child_aspect_ratio = 1.0,
                ),
                ft.Text(value = '2023', size = 30),
                ft.GridView(
                    controls = [image(num = num) for num in range(41, 51)],
                    runs_count = 5,
                    spacing = 5,
                    run_spacing = 5,
                    expand = True,
                    child_aspect_ratio = 1.0,
                ),
                ft.Text(value = '2024', size = 30),
                ft.GridView(
                    controls=[image(num = num) for num in range(52, 100)],
                    runs_count = 5,
                    spacing = 5,
                    run_spacing = 5,
                    expand = True,
                    child_aspect_ratio = 1.0,
                ),
            ],
        )

        navigation_buttons = ft.Container(
            content = ft.ResponsiveRow(
                columns = 12,
                controls = [
                    all_button := ft.ElevatedButton(
                        text = 'Todas as fotos',
                        bgcolor = ft.colors.GREY_900,
                        color = ft.colors.WHITE,
                        elevation = 0,
                        col = 6,
                        on_click = change_view,
                    ),
                    filter_button := ft.ElevatedButton(
                        text = 'Agrupadas',
                        bgcolor = ft.colors.GREY_500,
                        color = ft.colors.BLACK,
                        elevation = 0,
                        col = 6,
                        on_click = change_view,
                    ),
                ],
            ),
            bgcolor = ft.colors.GREY_500,
            height = 50,
            width = 500,
            border_radius = ft.border_radius.all(30),
            padding = ft.padding.all(10),
            alignment = ft.alignment.center
        )

        layout = ft.Container(
            content = ft.Column(
                controls = [
                    photo_grid_1,
                    navigation_buttons,
                ],
                alignment = ft.MainAxisAlignment.CENTER,
                horizontal_alignment = ft.CrossAxisAlignment.CENTER,
            ),
            gradient = ft.LinearGradient(
                begin = ft.alignment.top_center,
                end = ft.alignment.bottom_center,
                colors = ['#111827', '#000000'],
                stops = [0, 1],
            ),
            padding = ft.padding.all(20),
            expand = True,
        )

        self.page.add(layout)

if __name__ == '__main__':
    ft.app(target = App, assets_dir = 'assets')
