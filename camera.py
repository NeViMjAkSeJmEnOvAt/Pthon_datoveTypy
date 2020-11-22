class OtherCameras:
    gopro_hero_9 = 11900
    niceboy_vega_x_pro = 2990
    sencor_3cam = 679

class Camera:
    default_color = 'black'
    name_of_camera = 'SJ4000'
    price_camera = 1990
    wifi_camera = "yes"

    gopro = OtherCameras.gopro_hero_9
    niceboy = OtherCameras.niceboy_vega_x_pro
    sencor = OtherCameras.sencor_3cam

    def __init__ (self, obchod, cena):
        self.obchod = obchod
        self.cena = cena

        self.price = Camera.price_camera
        self.color = Camera.default_color
        self.name = Camera.name_of_camera
        self.wifi = Camera.wifi_camera

    def __str__(self):
        return f'({self.name}, {self.color}, {self.price}, {self.wifi} )'
    def Obchod(self):
        print("V obchodě " + self.obchod + " je cena kamery " + str(self.cena) + "kč")

    @classmethod
    def wifi(self, wifi_camera):
        if wifi_camera == "yes":
            return "Kamera má wifi"
        else:
            return "Kamera nemá kameru"

    @staticmethod
    def photo():
        max_photo_quality = "4032 x 3024"
        min_photo_quality = "640 x 480"
        print("Kamera fotí v rozlišení od: " + min_photo_quality + ", do: " + max_photo_quality)
    @staticmethod
    def video():
        max_resoluiton = "1080p 30fps"
        min_resolution = "720p 30fps"
        print("V režimu natáčení je kamera chopná točit v rozsahu: " + min_resolution + " až " + max_resoluiton)

    @staticmethod
    def soucetGopro(gopro, price_camera):
        return gopro - price_camera

    @staticmethod
    def soucetNiceboy(niceboy, price_camera):
        return niceboy - price_camera

    @staticmethod
    def soucetSencor(sencor, price_camera):
        vysledek_sencor = sencor - price_camera
        if vysledek_sencor < 0:
            vysledek_sencor = vysledek_sencor*(-1)
            return vysledek_sencor



print("Kamera " + Camera.name_of_camera + " s barvou: " + Camera.default_color)
Camera.photo()
Camera.video()
print("Gopro je o " + str(Camera.soucetGopro(Camera.gopro, Camera.price_camera)) + "Kč dražší než " + Camera.name_of_camera)
print("Niceboy je o " + str(Camera.soucetNiceboy(Camera.niceboy, Camera.price_camera)) + "Kč dražší než " + Camera.name_of_camera)
print("Sencor je o " + str(Camera.soucetSencor(Camera.sencor, Camera.price_camera)) + "Kč levnější než " + Camera.name_of_camera)
Datart = Camera("Datart", 1390)
MallCz = Camera("MallCz", 1990)
Sjcam = Camera("SjcamStore", 2300)
Datart.Obchod()
MallCz.Obchod()
Sjcam.Obchod()

