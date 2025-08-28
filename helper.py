expensetracker="""
MDLabel:
    text:"Expense Tracker"
    font_style:"H3"
    pos_hint:{'top':1.3}
    halign:'center'
    valign:'top'
    theme_text_color:"Hint"
"""

u_textField="""
MDTextField:
    hint_text:"Enter Email "
    size_hint_x: None
    helper_text:"or click on 'click here'"
    helper_text_mode:'on_focus'
    width: "200dp"
    valign:'top'
    pos_hint: {'bottom':0.5,"center_x": .5, "center_y": .5}
"""
p_textField="""
MDTextField:
    hint_text:"Enter Password "
    helper_text:"or click on 'click here'"
    helper_text_mode:'on_focus'
    size_hint_x: None
    width: "200dp"
    valign:'top'
    pos_hint: {"center_x": .5, "center_y": .2,'top':0.35,'bottom':0.5}
"""
l_button="""
MDRectangleFlatButton:
    text:"Login "
    pos_hint:{ "center_x":.45,"center_y": 0.37,'bottom':0.5,'right':0.8}
"""
signupButton="""
MDFlatButton:
    text:"Don't have an account? Click Here "
    pos_hint:{"center_x": .5,"center_y": 0.08}
    theme_text_color:"Primary"
"""