# tunn3l v1s10n
## Description
We found this file. Recover the [flag](https://mercury.picoctf.net/static/da18eed3d15fd04f7b076bdcecf15b27/tunn3l_v1s10n).
## Type: Forensics
## Solving
1) Download the file
2) Check the file by concatting the first few lines of file in cmd:

        head tunn3l_v1s10n
3) We can observe it starts with BM which tells us it could be a bitmap file (.bmp)
4) So I renamed the file and tried to open it but it showed that BMP image has unsupported header size.
5) So to open this file we can edit its header size by editing its hex.
6) For reference I downloaded a bitmap file’s hex.

![](/Forensics/tunn3l_v1s10n/tunn3l_v1s10n_resources/tv1.png)

7) I opened the file in [online Hex editor](https://hexed.it/) and edited its header size and offset of pixel data according to the above image and downloaded the new BMP file.
8) The file is displayed a image with a false flag and as the name of the problem suggested “tunnel vision” means the correct flag might be in the image but different area and now we are only focussing on a small area.
![](/Forensics/tunn3l_v1s10n/tunn3l_v1s10n_resources/tunn3l_v1s10n(2).bmp)
9) So now we have to edit the dimensions of the image, So I took reference from the above image and edited the height to 850 pixels using hexedior tool.
So heres my final hexcode after editing it:
![](/Forensics/tunn3l_v1s10n/tunn3l_v1s10n_resources/tv2.png)
The highlighted yellow cells are the cells which I edited.

10) After editing height I downloaded the BMP file again and found the flag on top of the image.
![](/Forensics/tunn3l_v1s10n/tunn3l_v1s10n_resources/tunn3l_v1s10n(1).bmp)


**Flag: picoCTF{qu1t3_a_v13w_2020}**