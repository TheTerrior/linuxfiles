# in order: reverse scroll direction, disable acceleration, decrease scroll speed, increase sensitivity
xinput set-prop "MSFT0001:01 04F3:3140 Touchpad" "libinput Natural Scrolling Enabled" 1 &
xinput set-prop "MSFT0001:01 04F3:3140 Touchpad" "libinput Accel Profile Enabled" 0, 1 &
xinput set-prop "MSFT0001:01 04F3:3140 Touchpad" "libinput Scrolling Pixel Distance" 50 &
xinput set-prop "MSFT0001:01 04F3:3140 Touchpad" "libinput Accel Speed" 0.5 &

picom --experimental-backends -b &
nitrogen --restore &
nm-applet &
pasystray --notify=none --notify=systray_action -g -m 100 &
copyq &
flameshot &
cbatticon -n &
/usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 &

