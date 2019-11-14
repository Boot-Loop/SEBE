
class SEBEFormTemplate:
    class Footer:
        def __init__(self, text, link_href, link_text):
            self.text       = text
            self.link_href  = link_href
            self.link_text  = link_text

    def __init__(self, title, submit_button_text='Submit', action='', footer_text='', footer_link_href='', footer_link_text=''):
        self.title              = title 
        self.submit_button_text = submit_button_text
        self.action             = action
        if footer_text != '':
            self.footer = SEBEFormTemplate.Footer( footer_text, footer_link_href, footer_link_text )
        else: 
            self.footer = None
