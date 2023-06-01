import justpy as jp
from webapp import layout


class About:
    path = "/about"

    def serve(self):
        wp = jp.QuasarPage(tailwind=True)

        lay = layout.DefaultLayout(a=wp)
        container = jp.QPageContainer(a=lay)

        div = jp.Div(a=container, classes="bg-gray-200 h-screen")
        jp.Div(a=div, text="This is the About page!", classes="text-4xl m-2")
        jp.Div(a=div, text="""
        Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor 
        incididunt ut labore et dolore magna aliqua. Volutpat diam ut venenatis tellus 
        in metus vulputate eu scelerisque. Sollicitudin tempor id eu nisl nunc mi 
        ipsum. Consequat interdum varius sit amet mattis vulputate enim nulla aliquet. 
        Vel quam elementum pulvinar etiam. Eget velit aliquet sagittis id consectetur 
        purus ut. Purus sit amet luctus venenatis. Pellentesque dignissim enim sit 
        amet venenatis urna cursus eget. Pellentesque habitant morbi tristique 
        senectus. Ullamcorper a lacus vestibulum sed arcu non odio euismod.
        """, classes="text-lg")
        return wp
