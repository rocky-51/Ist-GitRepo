expensetracker="""
MDScreen :
    md_bg_color : [35/255,59/255,54/255,1]
    MDCard :
        size_hint : None,None
        size : 800,600
        pos_hint : {"center_x":.5,"center_y":.5}
        elevation : 15
        md_bg_color : [50/255,50/255,50/255,1]
        padding : 20
        spacing : 30
        orientation : "vertical"
        MDLabel:
            text:"Expense Tracker"
            font_style:"H3"
            pos_hint:{'top':1.3}
            halign:'center'
            valign:'top'
            theme_text_color:"Hint"
        MDTextField:
            hint_text:"Enter Username "
            size_hint_x: None
            helper_text:"or click on 'click here'"
            helper_text_mode:'on_focus'
            width: "200dp"
            valign:'top'
            pos_hint: {'bottom':0.5,"center_x": .5, "center_y": .5}
        MDTextField:
            hint_text:"Enter Password "
            helper_text:"or click on 'click here'"
            helper_text_mode:'on_focus'
            size_hint_x: None
            width: "200dp"
            pos_hint: {"center_x": .5, "center_y": .3}
        MDRoundFlatButton :
            text : 'LOGIN'
            pos_hint : {"center_x":.5}
            font_size : 15
        MDFlatButton:
            text:"Don't have an account? Click Here "
            pos_hint:{"center_x": .5,"center_y": 0.08}
            theme_text_color:"Primary"
        Widget :
            size_hint_y : None
            height : 30
"""