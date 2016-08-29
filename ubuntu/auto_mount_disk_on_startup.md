# Automatically Mount a Disk on Startup

*from [Mitch](http://askubuntu.com/a/154185)*

First, list all the drives that are currently read by your computer with `sudo fdisk -l`. Identify where the device is mounted in the `/dev/` folder, for example `/dev/sdc1`.

Now, use the command `sudo blkid` to list all device IDs. Referencing the device mounted before (`/dev/sdc1`), find the associated UUID (`92B8CF29B8CF0AA5`).

Now, edit the `fstab` file to include this drive in the list of drives to mount at boot. First, back up the `fstab` file using `sudo cp /etc/fstab /etc/fstab.bkup`. Then, edit the `fstab` file using any text editor: `sudo nano /etc/fstab`.

Add a line like the below to your fstab file, then reboot the computer to test if it worked.
```
UUID=92B8CF29B8CF0AA5	/media/andy/HDD_2T	ntfs-3g	default	0	0
```
