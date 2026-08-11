from make_detailed_verified_3001_early_fragments_batch import write_batch

BATCHES = {
 1066:[('5223','002'),('5224','001'),('5224','002'),('5225','001'),('5225','002')],
 1067:[('5226','001'),('5226','002'),('5227','001'),('5228','001'),('5228','002')],
 1068:[('5229','001','Passio sanctorum Marciani et Martyrii notarii (BHG 1028y) (e cod. Hierosol. Sab.27, saec. xi)'),('5229','001','Passio sanctorum Marthae, Mariae et Lucarionis (BHG 2257) (e cod. Hierosol. 1)'),('5229','001','Acoluthia sancti Asclepiodotae (e cod. Vind. Theol. gr. 33)'),('5229','001','Passio Menodorae, Metrodorae et Nymphodorae (BHG 1272z) (e codice Athonensi Laurae Δ 50'),('5229','002')],
 1069:[('5230','001'),('5231','001'),('5233','001'),('5233','002'),('5233','003')],
 1070:[('5234','001'),('5234','002'),('5235','001'),('5236','001'),('5237','001')],
 1071:[('5238','001'),('5238','002'),('5239','001'),('5240','001'),('5241','001')],
 1072:[('5242','001'),('5243','001'),('5244','001'),('5244','002'),('5245','001')],
 1073:[('5246','001'),('5247','001'),('5248','001'),('5249','001'),('5250','001')],
 1074:[('5251','001'),('5251','144'),('5252','001'),('5253','001'),('5253','002')],
 1075:[('5254','001'),('5255','001'),('5255','002'),('5256','001'),('5257','001')],
 1076:[('5258','001'),('5259','001','Martyrium Bartholomaei apostoli (BHG 227)'),('5259','001','Martyrium sanctorum Carpi, Papyli et Agathonicae'),('5259','002','Reversio reliquiarum sancti apostoli Bartholomaei (fort. auctore Niceta Paphlagonio) (BHG 229), MPG 105: 213–217. Cod: 640: Hagiogr. Cf. et NICETAS David Paphlagonius Phil. et Scr. Eccl. (2705). 0390 VITAE CARPI, PAPYLI ET AGATHONICAE A.D. 2 Cf. et SYMEON Metaphrastes Hagiogr. et Hist. (3115 032)'),('5259','002','Martyrium sanctorum Carpi, Papyli et Agathonicae (BHG 294)')],
 1077:[('5260','001'),('5260','002'),('5260','003'),('5261','001'),('5261','002')],
 1078:[('5262','001'),('5262','002'),('5262','003'),('5263','001'),('5263','002')],
 1079:[('5264','001'),('5265','001'),('5265','002'),('5265','003'),('5265','004')],
 1080:[('5266','001'),('5267','001'),('5268','001'),('5268','002'),('5268','003')],
 1081:[('5268','004'),('5268','005'),('5268','006'),('5268','007'),('5269','001')],
 1082:[('5270','001'),('5271','001'),('5272','001'),('5273','001'),('5273','002')],
 1083:[('5273','003'),('5274','001'),('5274','002'),('5275','001'),('5275','002')],
 1084:[('5276','001'),('5277','001'),('5278','001'),('5279','001','Passio sanctorum Sergii et Bacchi (BHG 1624)'),('5279','001','Passio sanctorum Severi, Memnonis et aliorum (BHG 2399)')],
 1085:[('5279','001','Passio sanctorum Tarachi, Probi et Andronici (BHG [Novum Auctarium] 1574b) (e cods. Mosq. 161 Vlad. 379 et Hieros. Sab. gr. 30)'),('5280','001'),('5280','002'),('5281','001'),('5282','001')],
}

for number, targets in BATCHES.items():
    write_batch(f'data/research_batches/detailed_verified_3001_batch_{number}.csv', targets)
