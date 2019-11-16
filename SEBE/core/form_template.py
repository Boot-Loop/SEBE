
class SEBEFormTemplate:
    class Footer:
        def __init__(self, text, link_href, link_text):
            self.text       = text
            self.link_href  = link_href
            self.link_text  = link_text

    ''' if footer_link_herf is view-name pass is as django.urls.reverse(href) '''
    def __init__(self, title, submit_button_text='Submit', action='', 
        footer_text='', footer_link_href='', footer_link_text='', has_footer=True,
        safe_html_message = ''
        ):
        self.title              = title 
        self.submit_button_text = submit_button_text
        self.action             = action
        self.has_footer         = has_footer
        self.safe_html_message  = safe_html_message
        if has_footer:
            self.footer = SEBEFormTemplate.Footer( footer_text, footer_link_href, footer_link_text )
        else: 
            self.footer = None
