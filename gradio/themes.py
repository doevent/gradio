from gradio.theming.utils import Theme


class Default(Theme):
    def __init__(
        self,
        *,
        primary_hue="orange",
        secondary_hue="blue",
        neutral_hue="grey",
    ):

        self.color_accent_base = self._color(primary_hue, 500)
        self.color_accent_light = self._color(primary_hue, 300)
        self.color_accent_highlight = self._color(primary_hue, 700)

        self.color_border_primary = self._color(neutral_hue, 200)
        self.color_border_primary_dark = self._color(neutral_hue, 700)
        self.color_border_secondary = self._color(neutral_hue, 600)
        self.color_border_secondary_dark = self._color(neutral_hue, 600)
        self.color_border_highlight = self._use("color_accent_highlight")
        self.color_border_highlight_dark = self._use("color_accent_base")

        self.color_focus_primary = self._color(secondary_hue, 300)
        self.color_focus_primary_dark = self._color(secondary_hue, 700)
        self.color_focus_secondary = self._color(secondary_hue, 500)
        self.color_focus_secondary_dark = self._color(secondary_hue, 600)
        self.color_focus_ring = self._color(secondary_hue, 50)
        self.color_focus_ring_dark = self._color(secondary_hue, 950)

        self.color_background_primary = "white"
        self.color_background_primary_dark = self._color(neutral_hue, 950)
        self.color_background_secondary = self._color(neutral_hue, 50)
        self.color_background_primary_dark = self._color(neutral_hue, 900)
        self.color_background_tertiary = "white"
        self.color_background_tertiary_dark = self._color(neutral_hue, 800)

        self.color_text_body = self._color(neutral_hue, 800)
        self.color_text_body_dark = self._color(neutral_hue, 100)
        self.color_text_label = self._color(neutral_hue, 500)
        self.color_text_label_dark = self._color(neutral_hue, 200)
        self.color_text_placeholder = self._color(neutral_hue, 400)
        self.color_text_placeholder_dark = self._color(neutral_hue, 500)
        self.color_text_subdued = self._color(neutral_hue, 400)
        self.color_text_subdued_dark = self._color(neutral_hue, 400)
        self.color_text_link_base = self._color(secondary_hue, 600)
        self.color_text_link_base_dark = self._color(secondary_hue, 500)
        self.color_text_link_hover = self._color(secondary_hue, 700)
        self.color_text_link_hover_dark = self._color(secondary_hue, 400)
        self.color_text_link_visited = self._color(secondary_hue, 500)
        self.color_text_link_visited_dark = self._color(secondary_hue, 600)
        self.color_text_link_active = self._color(secondary_hue, 600)
        self.color_text_link_active_dark = self._color(secondary_hue, 500)
        self.color_text_code_background = self._color(neutral_hue, 200)
        self.color_text_code_background_dark = self._color(neutral_hue, 800)
        self.color_text_code_border = self._color(neutral_hue, 300)
        self.color_text_code_border_dark = self._use("color_border_primary_dark")

        self.color_functional_error_base = self._color("red", 500)
        self.color_functional_error_base_dark = self._color("red", 400)
        self.color_functional_error_subdued = self._color("red", 300)
        self.color_functional_error_subdued_dark = self._color("red", 300)
        self.color_functional_error_background = f"linear-gradient(to right,{self._color('red', 100)},{self.color_background_secondary})"
        self.color_functional_error_background_dark = self._use("color_background_primary_dark")
        self.color_functional_info_base = self._color("yellow", 500)
        self.color_functional_info_subdued = self._color("yellow", 300)
        self.color_functional_success_base = self._color("green", 500)
        self.color_functional_success_subdued = self._color("green", 300)

        self.shadow_drop = "rgba(0,0,0,0.05) 0px 1px 2px 0px"
        self.shadow_drop_lg = "0 1px 3px 0 rgb(0 0 0 / 0.1), 0 1px 2px -1px rgb(0 0 0 / 0.1)"
        self.shadow_drop_inset = "rgba(0,0,0,0.05) 0px 2px 4px 0px inset"

        self.block_label_border_color = self._use("color_border_primary")
        self.block_label_icon_color = self._use("color_text_label")
        self.block_label_background = self._use("color_background_primary")        
        self.icon_button_icon_color_base = self._use("color_text_label")
        self.icon_button_icon_color_hover = self._use("color_text_label")
        self.icon_button_background_base = self._use("color_background_primary")
        self.icon_button_background_hover = self._use("color_background_primary")
        self.icon_button_border_color_base = self._use("color_background_primary")
        self.icon_button_border_color_hover = self._use("color_border_primary")
        self.input_border_color_base = self._use("color_border_primary")
        self.input_border_color_hover = self._use("color_border_primary")
        self.input_border_color_focus = self._use("color_focus_primary")
        self.input_background_base = self._use("color_background_tertiary")
        self.input_background_hover = self._use("color_background_tertiary")
        self.input_background_focus = self._use("color_focus_tertiary")
        self.checkbox_border_radius = self._use("radius_sm")
        self.checkbox_border_color_base = self._color(neutral_hue, 300)
        self.checkbox_border_color_hover = self._color(neutral_hue, 300)
        self.checkbox_border_color_focus = self._color(secondary_hue, 500)
        self.checkbox_border_color_selected = self._color(secondary_hue, 600)
        self.checkbox_background_base = self._use("color_background_primary")
        self.checkbox_background_hover = self._use("color_background_primary")
        self.checkbox_background_focus = self._use("color_background_primary")
        self.checkbox_background_selected = self._color(secondary_hue, 600)
        self.checkbox_label_border_color_base = self._use("color_border_primary")
        self.checkbox_label_border_color_hover = self._use("color_border_primary")
        self.checkbox_label_border_color_focus = self._use("color_focus_secondary")
        self.checkbox_label_background_hover = f"linear-gradient(to top, {self._color('grey', 50)}, white)"
        self.checkbox_label_background_base = f"linear-gradient(to top, {self._color('grey', 50)}, white)"
        self.checkbox_label_background_focus = f"linear-gradient(to top, {self._color('grey', 100)}, white)"
        self.button_primary_border_color_base = self._color(primary_hue, 200)
        self.button_primary_border_color_hover = self._color(primary_hue, 200)
        self.button_primary_border_color_focus = self._color(primary_hue, 200)
        self.button_primary_text_color_base = self._color(primary_hue, 600)
        self.button_primary_text_color_hover = self._color(primary_hue, 600)
        self.button_primary_text_color_focus = self._color(primary_hue, 600)
        self.button_primary_background_base = f"linear-gradient(to bottom right, {self._color(primary_hue, 50)}, {self._color(primary_hue, 100)})"
        self.button_primary_background_hover = f"linear-gradient(to bottom right, {self._color(primary_hue, 100)}, {self._color(primary_hue, 200)})"
        self.button_primary_background_focus = f"linear-gradient(to bottom right, {self._color(primary_hue, 100)}, {self._color(primary_hue, 200)})"
        self.button_secondary_border_color_base = self._color(neutral_hue, 200)
        self.button_secondary_border_color_hover = self._color(neutral_hue, 200)
        self.button_secondary_border_color_focus = self._color(neutral_hue, 200)
        self.button_secondary_text_color_base = self._color("grey", 700)
        self.button_secondary_text_color_hover = self._color("grey", 700)
        self.button_secondary_text_color_focus = self._color("grey", 700)
        self.button_secondary_background_base = 'linear-gradient(to bottom right, rgb(243 244 246 / .7), rgb(229 231 235 / .8))'
        self.button_secondary_background_hover = 'linear-gradient(to bottom right, rgb(243 244 246 / .7), rgb(243 244 246 / .9))'
        self.button_secondary_background_focus = 'linear-gradient(to bottom right, rgb(243 244 246 / .7), rgb(243 244 246 / .9))'

        self.button_cancel_border_color_base = self._use("color_red_200")
        self.button_cancel_border_color_hover = self._use("color_red_200")
        self.button_cancel_border_color_focus = self._use("color_red_200")
        self.button_cancel_text_color_base = self._use("color_red_600")
        self.button_cancel_text_color_hover = self._use("color_red_600")
        self.button_cancel_text_color_focus = self._use("color_red_600")
        self.button_cancel_background_base = 'linear-gradient(to bottom right, rgb(254 202 202 / 0.7), rgb(252 165 165 / 0.8))'
        self.button_cancel_background_hover = 'linear-gradient(to bottom right, rgb(254 202 202 / 0.7), rgb(254 202 202 / 0.9))'
        self.button_cancel_background_focus = 'linear-gradient(to bottom right, rgb(254 202 202 / 0.7), rgb(254 202 202 / 0.9))'
        self.button_plain_border_color_base = self._use("color_border_primary")
        self.button_plain_border_color_hover = self._use("color_border_primary")
        self.button_plain_border_color_focus = self._use("color_border_primary")
        self.button_plain_text_color_base = self._use("color_text_body")
        self.button_plain_text_color_hover = self._use("color_text_body")
        self.button_plain_text_color_focus = self._use("color_text_body")
        self.button_plain_background_base = 'white'
        self.button_plain_background_hover = 'white'
        self.button_plain_background_focus = 'white'

        self.api_background = f"linear-gradient(to bottom, {self._color(primary_hue, 50)}, transparent)"
        self.api_pill_background = self._color(primary_hue, 100)
        self.api_pill_border = self._color(primary_hue, 200)
        self.api_pill_text = self._color(primary_hue, 600)
        self.gallery_label_background_base = self._use("color_grey_50")
        self.gallery_label_background_hover = self._use("color_grey_50")
        self.gallery_label_border_color_base = self._use("color_border_primary")
        self.gallery_label_border_color_hover = self._use("color_border_primary")
        self.gallery_thumb_background_base = self._color(neutral_hue, 100)
        self.gallery_thumb_background_hover = 'white'
        self.gallery_thumb_border_color_base = self._use("color_border_primary")
        self.gallery_thumb_border_color_hover = self._use("color_accent_light")
        self.gallery_thumb_border_color_focus = self._use("color_focus_secondary")
        self.gallery_thumb_border_color_selected = self._use("color_accent_base")
        self.chatbot_border_radius = self._use("radius_3xl")
        self.chatbot_border_width = '0'
        self.chatbot_user_background_base = self._color(primary_hue, 400)
        self.chatbot_user_background_latest = self._color(primary_hue, 400)
        self.chatbot_user_text_color_base = 'white'
        self.chatbot_user_text_color_latest = 'white'
        self.chatbot_user_border_color_base = 'transparent'
        self.chatbot_user_border_color_latest = 'transparent'
        self.chatbot_bot_background_base = self._color(neutral_hue, 400)
        self.chatbot_bot_background_latest = self._color(neutral_hue, 400)
        self.chatbot_bot_text_color_base = 'white'
        self.chatbot_bot_text_color_latest = 'white'
        self.chatbot_bot_border_color_base = 'transparent'
        self.chatbot_bot_border_color_latest = 'transparent'
        self.label_gradient_from = self._color(primary_hue, 400)
        self.label_gradient_to = self._color(primary_hue, 200)
        self.table_even_background = 'white'
        self.table_odd_background = self._use("color_grey_50")
        self.table_background_edit = self._use("color_orange_50")
        self.dataset_gallery_background_base = 'white'
        self.dataset_gallery_background_hover = self._use("color_grey_50")
        self.dataset_dataframe_border_base = self._color(neutral_hue, 300)
        self.dataset_dataframe_border_hover = self._color(neutral_hue, 300)
        self.dataset_table_background_base = 'transparent'
        self.dataset_table_background_hover = self._use("color_orange_50")
        self.dataset_table_border_base = self._use("color_border_primary")
        self.dataset_table_border_hover = self._color(primary_hue, 100)

