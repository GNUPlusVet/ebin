	

Same as Arch Linux, Gentoo is an Open Source meta-distribution build from sources, based on Linux Kernel, embracing the same rolling release model, aimed for speed and complete customizable for different hardware architectures which compiles software sources locally for best performance using an advanced package management – Portage.
Gentoo Installation Guide

Gentoo Linux Installation Guide

Because the final user can choose which components are to be installed, Gentoo Linux installation is a very difficult process for unexperienced users, but this tutorial uses for simplification a pre-build environment provided by a LiveDVD and a stage 3 tarball with minimal system software required to complete installation.

This tutorial shows you a step by step Gentoo installation simplified single-boot procedure, divided into two parts, using a 64-bit image with the last Stage 3 Tarball, using a GPT partition scheme and a customized Kernel image provided by Gentoo developers, so arm yourself with plenty of patience because installing Gentoo can be a long time consuming process.
Step 1: Download Gentoo DVD Image and Prepare Network Configurations

1. Before proceeding with installation go to Gentoo Download page and grab the last released LiveDVD image.

2. After you burn the ISO image place the DVD in your system DVD drive, reboot your computer, select your bootable DVD and Gentoo prompt LiveDVD should appear on your screen. Select the first option (Gentoo x86_64) which boots the default Gentoo Kernel then press Enter key to continue.
Boot Gentoo Live

Boot Gentoo Live

3. After Gentoo DVD content is loaded you will be prompted with Gentoo main login screen which provides the default credentials for live session. Press Enter to login then go to KDE start button and open a Terminal window.
Gentoo Desktop Login Screen

Login Screen
Open Terminal

Open Terminal

4. Now it’s time to check your network configuration and Internet connectivity using ifconfig command and ping against a domain. If you are behind a DHCP server, your network card should be automatically configured for you else use net-setup or pppoe-setup and pppoe-start commands or dhcpcd eth0 (replace it with your NIC plugged cable) in case your NIC has problems with automatically detect DHCP settings.

For static network configurations use the following commands but replace IPs according to your network settings.

$ sudo su -
# ifconfig eth0 192.168.1.100 broadcast 192.168.1.255 netmask 255.255.255.0 up
# route add default gw 192.168.1.1

# nano /etc/resolv.conf
nameserver 192.168.1.1
nameserver 8.8.8.8

Configure Network Connection

Configure Network Connection
Verify Network Connection

Verify Network Connection
Step 2: Create Disk Partitions and Filesystems

5. After you network connectivity has been established and confirmed it’s time to prepare Hard Disk. The following GPT partition layout will be used, but the same partition scheme can be also applied on a MBR BIOS disk using fdisk utility.

/dev/sda1 - 20M size – unformatted = BIOS boot partition
/dev/sda2 – 500M size – ext2 filesystem = Boot partition
/dev/sda3 - 1000M size – Swap = Swap partition
/dev/sda4 - rest of space – ext4 filesystem = Root Partition

To create system disk partition switch to root account and run Parted utility with optimum alignment.

$ sudo su -
# parted -a optimal /dev/sda

Create Disk Partitions

Create Disk Partitions

6. After entering parted CLI interface set GPT label on your hard disk.

# mklabel gpt

7. Use print to show your disk partition current state and remove any partitions (if case) using rm partition number command. Then supply parted with MB or mib size unit, create the first partition with mkpart primary, give it a name and set the boot flag on this partition.

(parted) unit MB
(parted) mkpart primary 1 20
(parted) name 1 grub
(parted) set 1 bios_grub on
(parted) print

Check Disk Partition

Check Disk Partition

The way that Parted deals with partition sizes is to tell it to start from 1MB + the desired value size (in this case start a 1 MB and end at 20 MB which results in a 19 MB partition size).

8. Then create all the partitions using the same method as above.
Boot Partition

(parted) mkpart primary 21 500
(parted) name 2 boot

Swap Partition

(parted) mkpart primary 501 1501
(parted) name 3 swap

Root Partition

(parted) mkpart primary 1502 -1
(parted) name 4 root

As you can see Root partition uses -1 as maximum value which means that it’s using all the remaining space -1 MB at the end of disk space. After you complete with disk slices use print to see your final partition layout (should look like in the image below) and quit parted.
Final Partition Layout

Final Partition Layout

9. Now it’s time to format partitions using a specific Linux filesystem, activate Swap file and mount Root and Boot partitions to /mnt/gentoo path.

# mkfs.ext2 /dev/sda2
# mkfs.ext4 /dev/sda4
# mkswap /dev/sda3
# swapon /dev/sda3

Format Partitions

Format Partitions
Mount Partitions

Mount Partitions
Step 3: Download and extract Gentoo Stage 3 Tarball

10. Before downloading Gentoo Stage 3 Tarball check your system time and date using date command and, in case, there’s a huge time desynchronization use the following syntax to synchronize time.

# date MMDDhhmmYYYY   ##(Month, Day, hour, minute and Year)

11. Now it’s time to download Gentoo Stage 3 Tarball. Proceed to /mnt/gentoo path and use links command to navigate to Gentoo Mirror list and select your Country nearest mirrors -> releases -> amd64 (or your system architecture) -> current-iso -> stage3-cpu-architecure-release-date.tar.bz2.

# cd /mnt/gentoo
# links http://www.gentoo.org/main/en/mirrors.xml

Gentoo Mirror List

Gentoo Mirror List
Select Nearest Mirror

Select Nearest Mirror
Select Your Architecture

Select Your Architecture
Select Current Gentoo ISO

Select Current Gentoo ISO
Download Gentoo Stage 3 Tarball

Download Gentoo Stage 3 Tarball

After selecting the Tarball press [Enter] key, select OK, wait for the download to finish and quit links.
Save Gentoo Stage 3 Tarball

Save Gentoo Stage 3 Tarball
Downloading Gentoo Stage 3 Tarball

Downloading Gentoo Stage 3 Tarball
Exit links Window

Exit links Window

12. On the next step, extract Stage 3 Tarball archive using the following command.

# tar xvjpf stage3-amb64-20140522.tar.bz2

Stage 3 Tarball File

Stage 3 Tarball File
Extract Stage 3 Tarball

Extract Stage 3 Tarball

Now you have a minimal Gentoo environment installed on your computer but the installation process is far from being finished. To continue the installation process follow Install Gentoo Linux – Part 2 tutorial.
Share
+
0
0
1
Ask Anything
If You Appreciate What We Do Here On TecMint, You Should Consider:

    Stay Connected to: Twitter | Facebook | Google Plus
    Subscribe to our email updates: Sign Up Now
    Get your own self-hosted blog with a Free Domain at ($3.95/month).
    Become a Supporter - Make a contribution via PayPal
    Support us by purchasing our premium books in PDF format.
    Support us by taking our online Linux courses

We are thankful for your never ending support.

Tags: gentoo

View all Posts

Matei Cezar

I'am a computer addicted guy, a fan of open source and linux based system software, have about 4 years experience with Linux distributions desktop, servers and bash scripting.

Your name can also be listed here. Got a tip? Submit it here to become an TecMint author.
RedHat RHCE and RHCSA Certification Book
Linux Foundation LFCS and LFCE Certification Preparation Guide

    Next story
    Understanding and Writing ‘Linux Variables’ in Shell Scripting – Part 10
    Previous story
    Practical Interview Questions and Answers on Linux Shell Scripting

You may also like...

    Install Skype in Gentoo Linux	
    0
    Skype 4.3 Released – Install on Gentoo Linux

    21 Jun, 2014
    Install FcgiWrap with Perl, Ruby and Bash	
    0
    Installing FcgiWrap and Enabling Perl, Ruby and Bash Dynamic Languages on Gentoo LEMP

    18 Jun, 2014
    Create Apache Virtual Hosts in Gentoo	
    0
    Creating Virtual Hosts, Generate SSL Certificates & Keys and Enable CGI Gateway in Gentoo Linux

    14 Jun, 2014

10 Responses

    Comments10
    Pingbacks0

    Lilian
    October 21, 2016 at 5:01 pm	

    Step 6.21
    # emerge gentoo-sources
    emerge: there are no ebuilds to satisfy “gentoo-sources”.

    Ce-i de facut?
    Reply
        Matei Cezar
        October 24, 2016 at 5:04 pm	

        emerge –sync
        Reply
    BORKBORK
    April 4, 2016 at 6:04 pm	

    I’m a Linux noob but Gentoo and Arch Linux just make me barf. It’s easier to to just repackage, re-brand and re-roll your own distro based on an existing one. The amount of time and punishment it takes to learn the Linux kernel, File system, Daemons, Partitions etc.. A newb like me would rather just based a distro on an existing one. It’s cheap, it’s dirty, it’s under handed but it’s free so why not.
    Reply
    Patrick P
    February 29, 2016 at 11:12 pm	

    What is the su – password???
    Reply
    GNU Rida
    August 18, 2015 at 9:10 am	

    Thanks! I used this guide to install Gentoo in the club!
    Reply
    esrin
    February 15, 2015 at 3:18 am	

    You forgot to include the step for mounting the partitions. There is just a screenshot but you skipped that step in your guide.

    Kinda ruined the whole guide for me because it seemed so thorough that I didn’t question it until I kept running out of space trying to install the kernel and had to go back only to see you completely left that step out. I finally found it in the tiny font of the screenshot.

    Good effort though but you should really fix that if you are going to call it an installation guide because without the step it makes it awfully confusing considering there is a step along with each screenshot for everything else. It’s supposed to be an installation guide “with” screenshots, right?
    Reply
    chaneng
    December 21, 2014 at 7:07 pm	

    Thanks for posting.
    It was very useful to me.
    I’m not linux specialist, so step-by-step manual is good for beginer.
    Thanks.
    Reply
    Chris
    December 3, 2014 at 7:14 am	

    Good luck i havent tried gentoo in ages it had an installer back then i believe this was hmm perhaps 7 years ago give or take now i miss it and its capabilities trying it again alongside my windows good luck CJ this guide makes it much easier in case a hiccup browser next to u for reference :) if using live dvd tat is
    Reply
    CJ
    September 10, 2014 at 4:19 am	

    I’ve attempted to install Gentoo at least a dozen times since 2005 and have met with failure each time. I recently decided to give it another try and I’m going to use your tutorials. Wish me luck.
    Reply
    Joe
    June 18, 2014 at 10:20 am	

    Wow! Very complicated but much appreciated. I just followed the links in this tutorial, and will do so again for part 2, but I learned a little bit. Thanks for posting this.
    Reply

Got something to say? Join the discussion.

Comment

Name *

Email *

Website

Notify me of followup comments via e-mail. You can also subscribe without commenting.

I TecMint :

BEGINNER'S GUIDE FOR LINUX Start learning Linux in minutes
Vi/Vim Editor BEGINNER'S GUIDE Learn vi/vim as a Full Text Editor
Linux Foundation Certification Exam Study Guide to LFCS and LFCE

    How to Add Linux Host to Nagios Monitoring Server Using NRPE Plugin

    Nagios 4.2.0 Released – Install on RHEL/CentOS 7.x/6.x/5.x and Fedora 24-19

    Install Cacti (Network Monitoring) on RHEL/CentOS 7.x/6.x/5.x and Fedora 24-12

    Google Chrome 58 Released – Install on RHEL/CentOS 7/6 and Fedora 25-20

    How to Install Ubuntu 16.10/16.04 Alongside With Windows 10 or 8 in Dual-Boot

    Tecmint’s Guide to Red Hat RHCSA / RHCE Certification Preparation Study Guide

RedHat RHCSA and RHCE Certification Exam Study Ebook

Linux System Administrator Bundle with 7-Courses (96% off)

Add to Cart - $69

Ending In: 3 days

Computer Hacker Professional Certification Course (96% Off)

Add to Cart - $59

Ending In: 4 days
Linux eBooks

    Introducing Learn Linux In One Week and Go from Zero to Hero
    RedHat RHCE/RHCSA Certification Preparation Guide
    Linux Foundations LFCS/LFCE Certification Guide
    Postfix Mail Server Setup Guide for Linux
    Ansible Setup Guide for Linux
    Django Setup Guide for Linux
    Awk Getting Started Guide for Beginners
    Citrix XenServer Setup Guide for Linux

Never Miss Any Linux Tutorials, Guides, Tips and Free eBooks

Join Our Community Of 150,000+ Linux Lovers and get a weekly newsletter in your inbox

YES! SIGN ME UP
Linux Monitoring Tools

    20 Netstat Commands for Linux Network Management

    Cockpit – A Powerful Tool to Monitor and Administer Multiple Linux Servers Using a Web Browser

    How to Install vnStat and vnStati to Monitor Network Traffic in RHEL/CentOS 7

    How to Monitor Apache Web Server Load and Page Statistics

    GoAccess (A Real-Time Apache and Nginx) Web Server Log Analyzer

Linux Interview Questions

    Basic Linux Interview Questions and Answers – Part II

    Nishita Agarwal Shares Her Interview Experience on Linux ‘iptables’ Firewall

    10 Linux Interview Questions and Answers for Linux Beginners – Part 3

    10 Useful Random Linux Interview Questions and Answers

    10 MySQL Database Interview Questions for Beginners and Intermediates

Open Source Tools

    5 Tools to Take or Capture Desktop Screenshots in Ubuntu Linux

    5 Most Frequently Used Open Source Shells for Linux

    10 Best Free and Open Source Software (FOSS) Programs I Found in 2016

    6 Best Email Clients for Linux Systems

    My Favorite Command Line Editors for Linux – What’s Your Editor?

