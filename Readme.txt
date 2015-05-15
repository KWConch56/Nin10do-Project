-------------------------------------------------------------------------------------------------------
-------------------------------------------------------------------------------------------------------
-------------------------------------------------------------------------------------------------------
----------------------------------o------NIN10DO PROJECT-----o-----------------------------------------
-------------------------------o-------------------------------o---------------------------------------
-----------------------------o----------------BY-----------------o-------------------------------------
-------------------------------o--------------------------------o--------------------------------------
--------------------------------o-------THE DANIEL SPIES------o----------------------------------------
-------------------------------------------------------------------------------------------------------
-------------------------------------------------------------------------------------------------------
--------------------------------  BASED ON THE RETROPIE PROJECT----------------------------------------
-------------------------------------------------------------------------------------------------------
--------------------------XXX---------------May 2015---------------XXX---------------------------------
-------------------------------------------------------------------------------------------------------
-------------------------------------------------------------------------------------------------------

Install Info:
----------------------------

1: Mount image file on SD card with 'WIN32DISKIMAGER' on your Windows PC
2: If you want to use a WIFI adapter go to the terminal: ('F4' key from Emulationstation then 'ENTER')
   type in: sudo nano /etc/wpa_supplicant/wpa_supplicant.conf
   Then fill in your ssid (network) name instead of 'YOUR NETWORK'
   fill in your WPA key instead of 'YOUR WPA KEY / PASSWORD'
   press 'CTRL+X' then 'Y' to save.
   Type: sudo reboot
   When prompted in Emulationstation hit 'F4' and 'ENTER' again and check if there is a IP address (red numbers) wrtitten in the Retopie logo

	Update: Now WIFI can be setup very easy within the RETROPIE menu in EMULATIONSTATION (above steps are no longer needed)

3: If you have black borders at the sides of your screen go to the terminal and type: sudo nano /boot/config.txt
   remove the # symbols to enable the over/under scan function. Standard settings are +16 for all borders. Change the numbers
   to -16 or more and reboot the system to see the result.
4: The Image comes with no ROMS installed. Install WinSCP and connect to the IP address of your Pi.
   Login: Pi Passwrd: Raspberry
   Open the /home/pi/retropie/roms folder and drag the ROMS (don't unzip!) to the correct folders.
5: The controls are already setup:
   EmulationStation: '+' and '-' are 'Select' and 'Start' / 'Enter' is 'A' / BACKSPACE is 'B'
   To setup new controllers or change the existing setup please go to the 'RETROPIE' function between the other emulators
   and choose the options for controller input.
   
check out the great video by 'Techtipstra' to learn how to setup controllers quick and easy.
Also check the great links in his description to free MAME and NEO GEO romsets.
link: https://www.youtube.com/watch?v=ySoTQhQqZdI
          

General Info:
-----------------------------

The image comes complete with:
- Nin10do Splash screen instead of the common boot text
- nin10do_script.py Python script pre-installed and started at boot ( /etc/rc.local )
- ATX Raspi shell script pre-installed and tweaked so the nin10do_script.py can finish closing the cover before the Pi
  is turned off (added 3 sec delay)
- NEO GEO BIOS file pre-installed in the FBA folder. (Be sure to use the correct romset!)
- Overclocking Enabled 'PI 2' setting at 1000mhz (2v over-volt)
- Exit emulator hotkeys pre-configured: press both the 'select' and 'start' keys on your controller to exit the emulator while in game.


Barendrecht, Holland
Mei 2015

TheDanielSpies
info@close-up-illusies.nl
 






