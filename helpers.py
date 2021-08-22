image_helper ="""
Image:
    source: 'first.png'
    pos_hint: {'center_x': 0.5, 'center_y': 0.8}
    size: .2, .2

"""

username_helper ="""
MDTextField:
    id: user
    hint_text: "Username"
    helper_text: "Forgot Username?"
    helper_text_mode: "on_focus"
    icon_right: "account"
    icon_right_color: app.theme_cls.primary_color
    pos_hint: {'center_x': 0.5, 'center_y': 0.4}
    size_hint_x: None
    width: 300
"""
password_helper ="""
MDTextField:
    id: pass
    hint_text: "Password"
    helper_text: "Forgot Password?"
    helper_text_mode: "on_focus"
    icon_right: "key"
    icon_right_color: app.theme_cls.primary_color
    pos_hint: {'center_x': .5, 'center_y': 0.3}
    size_hint_x: None
    width: 300
    password: True
"""


