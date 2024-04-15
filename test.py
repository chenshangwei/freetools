import flet as ft
import fitz

def main(page: ft.Page):
    pdfFile = {}
    def pick_files_result(e: ft.FilePickerResultEvent):
        selected_files.value = (
            ", ".join(map(lambda f: f.name, e.files)) if e.files else "已取消选择!"
        )
        pdfFile['name'] = e.files[0].name
        pdfFile['path'] = e.files[0].path
        print(pdfFile)
        selected_files.update()



    pick_files_dialog = ft.FilePicker(on_result=pick_files_result)
    selected_files = ft.Text()

    page.overlay.append(pick_files_dialog)
    def start(e):
        print(e)
        print('pdf_name',pdfFile['name'])
        print('pdf_path',pdfFile['path'])
        doc = fitz.open(pdfFile['path'])
        for page in doc:
            pix = page.get_pixmap(dpi=200) #,alpha=True
            pix.save("./%s-%i.png" % (pdfFile['name'],page.number))

    page.add(
        ft.Row(
            [
                ft.ElevatedButton(
                    "选择文件",
                    icon=ft.icons.UPLOAD_FILE,
                    on_click=lambda _: pick_files_dialog.pick_files(
                        allow_multiple=False
                    ),
                ),
                selected_files,
                ft.ElevatedButton(
                    "START",
                    icon=ft.icons.START_OUTLINED,
                    on_click=start,
                    disabled=False,
                ),
            ]
        )
    )

ft.app(target=main)
