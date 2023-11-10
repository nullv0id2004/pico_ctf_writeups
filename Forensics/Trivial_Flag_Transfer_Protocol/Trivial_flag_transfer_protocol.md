# Trivial Flag Transfer Protocol
## Description
Figure out how they moved the [flag](https://mercury.picoctf.net/static/4fe0f4357f7458c6892af394426eab55/tftp.pcapng).

## Type: Forensics

## Solving:
1) I downloaded the file and captured its packets on wireshark. I observed that it has a lot of TFTP protocol packets.
2) So I exported the TFTP objects and saved all the files in a folder.
3) I observed the files and there were 3 bmp image files and two text file and 1 deb file.
![](/Forensics/Trivial_Flag_Transfer_Protocol/Trivial_Flag_Transfer_Protocol_resources/img3.png)
4) I opened [instruction.txt](/Forensics/Trivial_Flag_Transfer_Protocol/Trivial_Flag_Transfer_Protocol_resources/instructions.txt) which seemed like a random jumble of letters probably a cipher. So I tested it by decrypting with one of the most widely used ceaser cypher (ROT13) using [CyberChef](https://gchq.github.io/CyberChef/#recipe=ROT13(true,true,false,13))
and i got a meaningful text:
**TFTP DOESNT ENCRYPT OUR TRAFFIC SO WE MUST DISGUISE OUR FLAG TRANSFER. FIGURE OUT A WAY TO HIDE THE FLAG AND I WILL CHECK BACK FOR THE PLAN.**
5) This gives us the hint that we can find something meaningful in the file [plan](/Forensics/Trivial_Flag_Transfer_Protocol/Trivial_Flag_Transfer_Protocol_resources/plan). So i opened plan.txt and which was also a jumble of letters so i used the same cypher to decypher it and i got some meaningful text:
**I USED THE PROGRAM AND HID IT WITH- DUEDILIGENCE. CHECK OUT THE PHOTOS.**
6) I found out that the program was steghide so i installed it using the command

        sudo apt install steghide
    Steghide is a steganography program that is able to hide data in various kinds of image- and audio-files.
![](/Forensics/Trivial_Flag_Transfer_Protocol/Trivial_Flag_Transfer_Protocol_resources/img4.png)
7) I found out how to use it in terminal by

        steghide --help
    ![](/Forensics/Trivial_Flag_Transfer_Protocol/Trivial_Flag_Transfer_Protocol_resources/img5.png)
8) So i have to extract the bmp images using steghide and the passphrase given is DUEDILIGENCE. So I extracted the file one by one using the command

        steghide –extract -sf picture1.bmp -p DUEDILIGENCE
    on extracting [picture3.bmp](/Forensics/Trivial_Flag_Transfer_Protocol/Trivial_Flag_Transfer_Protocol_resources/picture3.bmp) the extracted information was written on flag.txt. Then i concatted that file

        cat flag.txt
    
    ![](/Forensics/Trivial_Flag_Transfer_Protocol/Trivial_Flag_Transfer_Protocol_resources/img6.png)
    ![](/Forensics/Trivial_Flag_Transfer_Protocol/Trivial_Flag_Transfer_Protocol_resources/img7.png)

**Flag: picoCTF{h1dd3n_1n_pLa1n_51GHT_18375919}**