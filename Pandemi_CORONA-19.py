print("\t\t\t\tPANDEMI COVID-19 \n\tSIAPA YANG PERLU MELAKUKAN PEMERIKSAN KEEHATAN KERUMAH SAKIT\n")
tes1 = int(input("pernah kontak dengan pasien COVID-19 (berada dalam satu ruangan yang sama/kontak dalam jark 1 meter) Atau pernah berkunjung kenegara/daerah endemis COVID-19 dalam 14 hari terakhir ??? \n 1. YA \n 2. TIDAK \n your Answer :  "))
tes2 = int(input("sedang atau pernah mengalami : \n 1. Demam (>38 C) \n 2. pilek \n 3. batuk \n 4. sesak nafas\n\n 1. YA \n 2. TIDAK \n your Answer :   "))


if tes1 == 1:
    if tes2 == 1:
        print("hubungi 199 EXT 9 atau periksalah diri kerumah sakit rujukan COVID-19 di daerah anda")
    elif tes2 == 2:
        print("karantina diri anda selama 14 hari terhitung setelah kontak/kunjungan \n") 
        tes6 = int(input("selama 14 hari karantina diri, anda mengalami : \n 1. Demam (>38 C) \n 2. pilek \n 3. batuk \n 4. sesak nafas\n 1. YA \n 2. TIDAK \n your Answer :  "))
        if tes6 == 1:
            print ("hubungi 199 EXT 9 atau periksalah diri kerumah sakit rujukan COVID-19 di daerah anda")
        elif tes6 == 2:
            print ("anda tidak perlu memeriksakn diri kerumah sakit. selalu jaga kesehatan anda")
elif tes1 == 2:
    if tes2 == 1:
        print("periksalah diri anda ke dokter terdekat dan istirahatlah yang cukup")
    elif tes2 == 2:
        print("anda tidak perlu memeriksakn diri kerumah sakit. selalu jaga kesehatan anda")
else:
    print("slhkan_keluar_dari_program")
