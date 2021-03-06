###################################################################
#  elements of mhome app, include button, xpath, etc.
###################################################################

############################ login ################################
cancel_btn_id = "com.changhong.mhome:id/cancel_btn"

tel_xpath = '//android.widget.LinearLayout[1]/android.widget.LinearLayout/\
    android.widget.LinearLayout/android.widget.EditText'
pwd_xpath = '//android.widget.LinearLayout[2]/android.widget.LinearLayout/\
    android.widget.LinearLayout/android.widget.EditText'

regist_btn = 'com.changhong.mhome:id/btn_register'
login_btn = "com.changhong.mhome:id/btn_login"
forget_btn = 'com.changhong.mhome:id/btn_forget_passwd'

qqlogin_btn = 'com.changhong.mhome:id/btn_qq'   #press jump to qq login page
qq_confirm_btn = 'android.widget.Button'        #press confirm btn on qqlogin page

############################ main #################################
me_id = 'com.changhong.mhome:id/bm_btn_me'
setting_id = 'com.changhong.mhome:id/i_setting_me'
quit_btn = 'com.changhong.mhome:id/quit'
confirm_btn_id = 'com.changhong.mhome:id/confirm_btn' #include delete confirm
guide_img = 'com.changhong.mhome:id/guide_img'

############################ anniv ################################
ann_btn = 'com.changhong.mhome:id/btn_anniversary'    #jump to ann page
add_btn = 'com.changhong.mhome:id/header_btnrt'
ann_date_exist = 'com.changhong.mhome:id/txt_anni_day'#date on ann list page
ann_del_title = "com.changhong.mhome:id/title"        #delete alert's title
back_btn = "com.changhong.mhome:id/header_btnback"
swipe_del = 'com.changhong.mhome:id/layout_right'

#add anniversary page element
ann_title_et = 'com.changhong.mhome:id/edit_name'
ann_date_btn = 'com.changhong.mhome:id/btn_time'
ann_remind_time_btn = 'com.changhong.mhome:id/btn_remind_time'
remind_time_confirm = 'com.changhong.mhome:id/btn_gender_comfirm'

##remind day
ann_remind_day_btn = 'com.changhong.mhome:id/btn_remind_day'
remind_day_xpath = '//android.widget.LinearLayout'
remind_day_id = "com.changhong.mhome:id/selected"
done_btn = "com.changhong.mhome:id/done"            #confirm remind day
##date
lunnar_swap = 'com.changhong.mhome:id/img_swap'
date_year_view = 'com.changhong.mhome:id/wheel_view_year'
date_month_view = 'com.changhong.mhome:id/wheel_view_month'
date_day_view = 'com.changhong.mhome:id/wheel_view_day'
date_confirm = 'com.changhong.mhome:id/btn_comfirm'

##icon
ann_icon_btn = 'com.changhong.mhome:id/ll_icon'
icon_xpath = remind_day_xpath
icon_id = "com.changhong.mhome:id/select_img"

ann_item_xpath = remind_day_xpath
