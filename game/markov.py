import random

males = [
'Azarain', 'Azarath', 'Azarfar', 'Azarien', 'Azarik', 'Azaril', 'Azarimal', 'Azarimar', 'Azarkan', 'Azaron', 
'Azarpar', 'Azarseth', 'Casain', 'Casath', 'Casfar', 'Casien', 'Casik', 'Casil', 'Casimal', 'Casimar', 'Caskan', 'Cason', 
'Caspar', 'Casseth', 'Erebain', 'Erebath', 'Erebfar', 'Erebien', 'Erebik', 'Erebil', 'Erebimal', 'Erebimar', 'Erebkan', 
'Erebon', 'Erebpar', 'Erebseth', 'Helain', 'Helath', 'Helfar', 'Helien', 'Helik', 'Helil', 'Helimal', 'Helimar', 'Helkan', 
'Helon', 'Helpar', 'Helseth', 'Nisain', 'Nisath', 'Nisfar', 'Nisien', 'Nisik', 'Nisil', 'Nisimal', 'Nisimar', 'Niskan', 
'Nison', 'Nispar', 'Nisseth', 'Shalain', 'Shalath', 'Shalfar', 'Shalien', 'Shalik', 'Shalil', 'Shalimal', 'Shalimar', 
'Shalkan', 'Shalon', 'Shalpar', 'Shalseth', 'Shurain', 'Shurath', 'Shurfar', 'Shurien', 'Shurik', 'Shuril', 'Shurimal', 
'Shurimar', 'Shurkan', 'Shuron', 'Shurpar', 'Shurseth', 'Turain', 'Turath', 'Turfar', 'Turien', 'Turik', 'Turil', 'Turimal', 
'Turimar', 'Turkan', 'Turon', 'Turpar', 'Turseth', 'Ulain', 'Ulath', 'Ulfar', 'Ulien', 'Ulik', 'Ulil', 'Ulimal', 'Ulimar', 
'Ulkan', 'Ulon', 'Ulpar', 'Ulseth', 'Vanikain', 'Vanikath', 'Vanikfar', 'Vanikien', 'Vanikik', 'Vanikil', 'Vanikimal', 
'Vanikimar', 'Vanikkan', 'Vanikon', 'Vanikpar', 'Vanikseth', 'Zanain', 'Zanath', 'Zanfar', 'Zanien', 'Zanik', 'Zanil', 
'Zanimal', 'Zanimar', 'Zankan', 'Zanon', 'Zanpar', 'Zanseth', 'Zirain', 'Zirath', 'Zirfar', 'Zirien', 'Zirik', 'Ziril', 
'Zirimal', 'Zirimar', 'Zirkan', 'Ziron', 'Zirpar', 'Zirseth',

'Adaves', 'Adil', 'Adondasi', 'Adosi', 'Adren', 'Alam', 'Alanil', 'Aldam', 'Alds', 'Alms', 'Alnas', 'Alvan', 'Alven', 
'Alvis', 'Alvor', 'Alvos', 'Alvur', 'Anas', 'Anden', 'Andril', 'Anel', 'Angaredhel', 'Aras', 'Arelvam', 'Aren', 'Arethan', 
'Arnas', 'Aroa', 'Aron', 'Arsyn', 'Arven', 'Arver', 'Arvs', 'Arvyn', 'Aryon', 'Athal', 'Athanden', 'Athelyn', 'Ather', 
'Athyn', 'Avron', 'Baladas', 'Balver', 'Balyn', 'Banden', 'Banor', 'Baren', 'Barusi', 'Bedal', 'Belas', 'Beldrose', 
'Belos', 'Bels', 'Belvis', 'Benar', 'Beraren', 'Berel', 'Berela', 'Bertis', 'Bervaso', 'Bervyn', 'Bethes', 'Bevadar', 
'Bildren', 'Bilen', 'Bilos', 'Birer', 'Bolayn', 'Boler', 'Bolnor', 'Bols', 'Bolvus', 'Bolvyn', 'Bolyn', 'Boryn', 
'Bradil', 'Bralas', 'Bralen', 'Bralis', 'Bralyn', 'Brarayni', 'Bratheru', 'Brathus', 'Bravosi', 'Braynas', 'Brelar', 
'Brelo', 'Brelyn', 'Brerama', 'Brethas', 'Breves', 'Breynis', 'Briras', 'Broder', 'Broris', 'Brothes', 'Dalam', 'Daldur', 
'Dalin', 'Dalmil', 'Dalos', 'Dals', 'Dalvus', 'Danar', 'Dandras', 'Danel', 'Daral', 'Daras', 'Daren', 'Darns', 'Daroder', 
'Dartis', 'Darvam', 'Daryn', 'Dather', 'Dathus', 'Davas', 'Davis', 'Davur', 'Daynes', 'Daynil', 'Dedaenc', 'Delmon', 
'Delmus', 'Delvam', 'Deras', 'Dethresa', 'Deval', 'Devas', 'Dils', 'Dinor', 'Dirver', 'Divayth', 'Dolmyn', 'Dolyn', 
'Dondos', 'Donus', 'Dovor', 'Dovres', 'Dralas', 'Drals', 'Dralval', 'Dram', 'Dramis', 'Drandryn', 'Dranos', 'Drarayne', 
'Drarel', 'Draron', 'Drarus', 'Draryn', 'Drathyn', 'Dravasa', 'Dredase', 'Drelayn', 'Drelis', 'Drelse', 'Drerel', 
'Dreynis', 'Dreynos', 'Dridas', 'Dridyn', 'Drinar', 'Drodos', 'Dronos', 'Drores', 'Drulvan', 'Duldrar', 'Dunel', 'Edd', 
'Edras', 'Edril', 'Elam', 'Eldil', 'Eldrar', 'Elethus', 'Elms', 'Elo', 'Elvas', 'Elvil', 'Endar', 'Endris', 'Endryn', 
'Endul', 'Erene', 'Erer', 'Ereven', 'Eris', 'Ernil', 'Erns', 'Ervas', 'Ethes', 'Ethys', 'Evo', 'Evos', 'Fadren', 'Falam', 
'Falso', 'Falvel', 'Falvis', 'Farvam', 'Farvyn', 'Favas', 'Favel', 'Faven', 'Faver', 'Faves', 'Fedar', 'Felayn', 'Felen', 
'Felisi', 'Felsen', 'Felvan', 'Felvos', 'Femer', 'Fendros', 'Fendryn', 'Feranos', 'Ferele', 'Feril', 'Feruren', 'Fervas', 
'Fevris', 'Fevus', 'Fevyn', 'Folms', 'Folvys', 'Folyni', 'Fons', 'Fonus', 'Forven', 'Foryn', 'Fothas', 'Fothyna', 'Foves', 
'Fovus', 'Gadayn', 'Gaelion', 'Galam', 'Galdres', 'Galen', 'Galis', 'Galmis', 'Galms', 'Gals', 'Gamin', 'Ganalyn', 'Ganus', 
'Garer', 'Garisa', 'Garnas', 'Garvs', 'Garyn', 'Gathal', 'Gavas', 'Gavesu', 'Gavis', 'Gidar', 'Giden', 'Gilan', 'Gilmyn', 
'Gilur', 'Gilvas', 'Gilyan', 'Gilyn', 'Gilyne', 'Gindas', 'Ginur', 'Giras', 'Giren', 'Giron', 'Giryn', 'Golar', 'Goldyn', 
'Goler', 'Gols', 'Golven', 'Goras', 'Gordol', 'Goren', 'Goris', 'Goron', 'Gothren', 'Goval', 'Gragus', 'Gulmon', 'Guls', 
'Guril', 'Helseth', 'Hlaren', 'Hlaroi', 'Hlenil', 'Hleras', 'Hloris', 'Hort', 'Idros', 'Ildos', 'Ilen', 'Ilet', 'Ilver', 
'Iner', 'Irarak', 'Irer', 'Irver', 'Ivulen', 'Jiub', 'Llaals', 'Llanas', 'Llandras', 'Llandris', 'Llanel', 'Llarar', 
'Llarel', 'Llaren', 'Llaro', 'Llavam', 'Lleran', 'Lleras', 'Lleris', 'Llero', 'Llether', 'Llevas', 'Llevel', 'Lliram', 
'Lliros', 'Lliryn', 'Lloden', 'Llonas', 'Llondryn', 'Lloros', 'Llovyn', 'Madran', 'Madres', 'Madsu', 'Malar', 'Mallam', 
'Mals', 'Manabi', 'Mandran', 'Mandur', 'Mandyn', 'Manel', 'Maner', 'Manolos', 'Marayn', 'Maros', 'Mastrius', 'Mathis', 
'Mathyn', 'Mavis', 'Mavon', 'Mavus', 'Meder', 'Medyn', 'Melar', 'Melur', 'Menus', 'Meril', 'Mertis', 'Mertisi', 'Mervis', 
'Mervs', 'Meryn', 'Methal', 'Methas', 'Mevel', 'Meven', 'Mevil', 'Midar', 'Milar', 'Mils', 'Milyn', 'Miner', 'Miron', 'Mirvon', 
'Mivul', 'Mondros', 'Movis', 'Muvis', 'Nads', 'Nalis', 'Nalmen', 'Nalosi', 'Nals', 'Nalur', 'Naral', 'Naris', 'Nathyn', 'Navam', 
'Navil', 'Neldris', 'Nelmil', 'Nelos', 'Neloth', 'Nels', 'Nelvon', 'Nelyn', 'Nerer', 'Nethyn', 'Nevil', 'Nevon', 'Nevos', 'Nevosi', 
'Niden', 'Nilas', 'Nilos', 'Niras', 'Nivel', 'Nivos', 'Norus', 'Odral', 'Odron', 'Oisig', 'Ondar', 'Ondres', 'Orns', 'Orval', 
'Orvas', 'Ovis', 'Ralam', 'Ralds', 'Ralmyn', 'Ralos', 'Ranes', 'Ranor', 'Rararyn', 'Raril', 'Raryn', 'Rathal', 'Raviso', 
'Ravos', 'Raynilie', 'Relam', 'Relas', 'Relen', 'Relms', 'Rels', 'Relur', 'Relyn', 'Remas', 'Rernel', 'Reron', 'Rervam', 
'Reynis', 'Rilas', 'Rilos', 'Rilver', 'Rindral', 'Rirnas', 'Rirns', 'Rivame', 'Rolis', 'Rols', 'Roner', 'Rothis', 'Rovone', 
'Sadas', 'Sadryn', 'Salas', 'Salen', 'Salvas', 'Salver', 'Salyn', 'Sanvyn', 'Saras', 'Sarayn', 'Sarvil', 'Sarvur', 'Saryn', 
'Sathas', 'Savor', 'Savure', 'Sedam', 'Sedrane', 'Seldus', 'Seler', 'Selman', 'Selmen', 'Selvil', 'Sendel', 'Sendus', 
'Seras', 'Serer', 'Serul', 'Seryn', 'Sevilo', 'Shashev', 'Sodres', 'Sortis', 'Sovor', 'Stlennius', 'Sulen', 'Sulis', 
'Sunel', 'Sur', 'Suryn', 'Suvryn', 'Svadstar', 'Tadas', 'Talms', 'Tandram', 'Tanel', 'Tanur', 'Tarar', 'Tarer', 'Taros', 
'Tarvus', 'Tarvyn', 'Taves', 'Tedril', 'Tedryn', 'Tedur', 'Telis', 'Tels', 'Telvon', 'Temis', 'Tendren', 'Tendris', 'Tens', 
'Terer', 'Teres', 'Teris', 'Tervur', 'Tevyn', 'Thadar', 'Thaden', 'Thanelen', 'Tharer', 'Thauraver', 'Theldyn', 'Thervam', 
'Tholer', 'Thoryn', 'Threvul', 'Tidras', 'Tidros', 'Tinos', 'Tiram', 'Tiras', 'Tirer', 'Tirnur', 'Tirvel', 'Tivam', 'Toris', 
'Tralas', 'Tralayn', 'Traven', 'Tredyn', 'Trelam', 'Trels', 'Trendrus', 'Treram', 'Treras', 'Trevyn', 'Trilam', 'Trivon', 'Tuls', 
'Ultis', 'Ulves', 'Ulvil', 'Ulvon', 'Unel', 'Uradras', 'Ureval', 'Urnel', 'Urvel', 'Urven', 'Uryn', 'Uthrel', 'Uvele', 'Uvren', 
'Vaden', 'Vanel', 'Vares', 'Varis', 'Varon', 'Varvur', 'Vatollia', 'Vaves', 'Vavran', 'Vedam', 'Vedran', 'Velis', 'Velms', 
'Velyn', 'Veros', 'Vevos', 'Vevul', 'Vilval', 'Vilyn', 'Viras', 'Virvyn', 'Vobend', 'Vonden', 'Vonos', 'Vorar', 'Voruse', 'Vuvil'

]

females = [
'Cruatah', 'Cruelle', 'Cruethys', 'Cruiah', 'Cruinah', 'Cruith', 'Cruithah', 'Cruivah', 'Cruobah', 'Cruonah', 'Cruothah', 'Cruth',
'Dematah', 'Demelle', 'Demethys', 'Demiah', 'Deminah', 'Demith', 'Demithah', 'Demivah', 'Demobah', 'Demonah', 'Demothah', 'Demth',
'Golgatah', 'Golgelle', 'Golgethys', 'Golgiah', 'Golginah', 'Golgith', 'Golgithah', 'Golgivah', 'Golgobah', 'Golgonah', 'Golgothah', 'Golgth',
'Hekatah', 'Hekelle', 'Hekethys', 'Hekiah', 'Hekinah', 'Hekith', 'Hekithah', 'Hekivah', 'Hekobah', 'Hekonah', 'Hekothah', 'Hekth',
'Lilatah', 'Lilelle', 'Lilethys', 'Liliah', 'Lilinah', 'Lilith', 'Lilithah', 'Lilivah', 'Lilobah', 'Lilonah', 'Lilothah', 'Lilth',
'Lolatah', 'Lolelle', 'Lolethys', 'Loliah', 'Lolinah', 'Lolith', 'Lolithah', 'Lolivah', 'Lolobah', 'Lolonah', 'Lolothah', 'Lolth',
'Nephatah', 'Nephelle', 'Nephethys', 'Nephiah', 'Nephinah', 'Nephith', 'Nephithah', 'Nephivah', 'Nephobah', 'Nephonah', 'Nephothah', 'Nephth',
'Shelatah', 'Shelelle', 'Shelethys', 'Sheliah', 'Shelinah', 'Shelith', 'Shelithah', 'Shelivah', 'Shelobah', 'Shelonah', 'Shelothah', 'Shelth',
'Sheratah', 'Sherelle', 'Sherethys', 'Sheriah', 'Sherinah', 'Sherith', 'Sherithah', 'Sherivah', 'Sherobah', 'Sheronah', 'Sherothah', 'Sherth',
'Tabatah', 'Tabelle', 'Tabethys', 'Tabiah', 'Tabinah', 'Tabith', 'Tabithah', 'Tabivah', 'Tabobah', 'Tabonah', 'Tabothah', 'Tabth',
'Vaynatah', 'Vaynelle', 'Vaynethys', 'Vayniah', 'Vayninah', 'Vaynith', 'Vaynithah', 'Vaynivah', 'Vaynobah', 'Vaynonah', 'Vaynothah', 'Vaynth',
'Vermatah', 'Vermelle', 'Vermethys', 'Vermiah', 'Verminah', 'Vermith', 'Vermithah', 'Vermivah', 'Vermobah', 'Vermonah', 'Vermothah', 'Vermth',

'Aamela', 'Aamrila', 'Aarela', 'Adansa', 'Adosi', 'Adrasi', 'Adryn', 'Aerona', 'Aeyne', 'Alalura', 'Alaru', 
'Aldyna', 'Aldyne', 'Alicon', 'Alli', 'Alma', 'Almise', 'Almse', 'Alsal', 'Alurami', 'Alurue', 'Alves', 'Alvesi', 
'Alvila', 'Alvura', 'Amila', 'Amili', 'Andilan', 'Andilo', 'Aneyda', 'Ani', 'Anila', 'Anisa', 'Aphia', 'Aralosi', 
'Arara', 'Arela', 'Areyne', 'Arilu', 'Arisa', 'Arns', 'Arnsi', 'Arvena', 'Aryvena', 'Aspera', 'Athesa', 'Aurona', 
'Aymillo', 'Badila', 'Badilia', 'Bala', 'Balsia', 'Bameli', 'Bameni', 'Banda', 'Bedena', 'Bedyna', 'Bedyni', 'Belderi', 
'Belera', 'Beleru', 'Belosi', 'Belya', 'Bendyni', 'Bera', 'Berada', 'Berari', 'Berela', 'Betina', 'Betya', 'Beyte', 
'Bidia', 'Bidsa', 'Biiri', 'Bili', 'Binayne', 'Birila', 'Bivala', 'Bivale', 'Bivessa', 'Blivisi', 'Boderi', 'Boderia', 
'Boldrisa', 'Bolnora', 'Bothisii', 'Bralsa', 'Bralsi', 'Bravaria', 'Bravora', 'Breda', 'Bredami', 'Brela', 'Brelaca', 
'Brelayne', 'Brelda', 'Brelyn', 'Brelynd', 'Brema', 'Breva', 'Burila', 'Buronii', 'Butheli', 'Byla', 'Cadiva', 'Cindiri', 
'Cloya', 'Daela', 'Dala', 'Dalami', 'Daliina', 'Dalmi', 'Dalnorea', 'Dalora', 'Dalsa', 'Dalsi', 'Damisi', 'Dandea', 
'Dandrii', 'Danis', 'Darane', 'Darili', 'Daroso', 'Darva', 'Dasila', 'Dathlyn', 'Davilia', 'Dayas', 'Daymi', 'Dayna', 
'Dayni', 'Delatha', 'Deldasa', 'Delte', 'Dematah', 'Denu', 'Derami', 'Deria', 'Dervera', 'Diina', 'Dileni', 'Dilyne', 
'Dinaria', 'Dinuro', 'Dirilu', 'Dithisi', 'Dolsia', 'Domi', 'Donta', 'Dorisa', 'Dovesi', 'Dradas', 'Drala', 'Dralosa', 
'Drarana', 'Dratha', 'Drathyra', 'Dravusa', 'Drayna', 'Dredena', 'Dredyni', 'Dreska', 'Drilame', 'Drissa', 'Drivanas', 
'Drurile', 'Dunveril', 'Durena', 'Duroni', 'Edrasa', 'Edrisi', 'Edryn', 'Edwina', 'Eldri', 'Elmera', 'Elneri', 'Elvasia', 
'Elyna', 'Elynisi', 'Enura', 'Erila', 'Erivase', 'Eroni', 'Ervyla', 'Ervyna', 'Ervyni', 'Ervynu', 'Evessa', 'Evisi', 'Evylu', 
'Falan', 'Falora', 'Faltha', 'Famdii', 'Famyne', 'Faral', 'Faras', 'Farena', 'Faric', 'Farona', 'Faryon', 'Farys', 'Favel', 
'Favela', 'Fealu', 'Fedrasa', 'Feduria', 'Feldrasa', 'Feldsii', 'Felisa', 'Felmina', 'Felsa', 'Fenila', 'Ferdyn', 'Ferena', 
'Ferva', 'Fethesena', 'Fevila', 'Feyne', 'Fieria', 'Filu', 'Fonari', 'Fondryn', 'Foni', 'Fonira', 'Forvse', 'Furoni', 'Furu', 
'Fyrayn', 'Fyrona', 'Gadila', 'Gadsi', 'Galdas', 'Galdsa', 'Galisa', 'Galori', 'Galotha', 'Galsi', 'Galsu', 'Galyn', 'Gami', 
'Gandilla', 'Gariasa', 'Garila', 'Garyne', 'Gelaa', 'Gelana', 'Gelii', 'Gena', 'Gindur', 'Girara', 'Girva', 'Glistel', 'Godyna', 
'Golmerea', 'Golvy', 'Gorili', 'Grona', 'Guroanii', 'Guronii', 'Gynisi', 'Hadrill', 'Hala', 'Hanala', 'Helma', 'Helseth', 'Hlana', 
'Hlaren', 'Hlava', 'Hlavora', 'Hlenia', 'Hlethena', 'Hlevala', 'Hlisi', 'Hlura', 'Idrasa', 'Idrenia', 'Idria', 'Idroni', 'Idula', 
'Ienasa', 'Iirila', 'Ildari', 'Ildrasai-daro', 'Ilmeni', 'Indra', 'Indrasa', 'Indrasi', 'Indrela', 'Indrele', 'Indririi', 'Ineria', 
'Inisa', 'Inise', 'Iriana', 'Irileth', 'Iry', 'Isabeau', 'Ithrini', 'Ivaynel', 'Ivela', 'Ivramia', 'Ivrosa', 'Jenassa', 'Jinrisa', 
'Kalara', 'Kalina', 'Kireth', 'Kylia', 'Ladrasa', 'Lalis', 'Lathisa', 'Lauravenya', 'Laureva', 'Lena', 'Leyla', 'Lilyamah', 'Lirielle', 
'Lirona', 'Livisii', 'Llaals', 'Llaami', 'Llaari', 'Llarevis', 'Llasi', 'Llavana', 'Llavelea', 'Llayne', 'Llivas', 'Llivia', 'Llotha', 
'Llunela', 'Lodyna', 'Lolethys', 'Lorara', 'Lorolu', 'Louna', 'Luranor', 'Luryne', 'Madrana', 'Madria', 'Madura', 'Maedini', 'Maera', 
'Malarel', 'Malori', 'Mamyne', 'Maralie', 'Marasa', 'Mari', 'Mariia', 'Marila', 'Marilia', 'Marlyn', 'Marona', 'Maronii', 'Marwyn', 
'Mathesa', 'Melila', 'Meluria', 'Meralys', 'Meram', 'Merilar', 'Merona', 'Methulu', 'Meva', 'Mevura', 'Midrasi', 'Miiga', 'Miirist', 
'Milesa', 'Milia', 'Milore', 'Milva', 'Milvonu', 'Milyne', 'Mindelyn', 'Mirasa', 'Mirise', 'Mirnsa', 'Mirri', 'Mirusu', 'Mivani', 
'Mivanu', 'Mivryna', 'Morami', 'Morusu', 'Morvani', 'Mulvi', 'Murela', 'Muvulrea', 'Mylis', 'Myn', 'Nadie', 'Nalvyna', 'Nandri', 
'Nara', 'Nareb', 'Nareen', 'Naresa', 'Narese', 'Narilii', 'Narisa', 'Nartisa', 'Naryu', 'Nashyv', 'Nathyne', 'Nedi', 'Nedrasa', 
'Nela', 'Nelmia', 'Neloren', 'Nelvana', 'Nendrii', 'Nerari', 'Neria', 'Nervyna', 'Nevusa', 'Neyna', 'Nida', 'Nila', 'Nilonii', 
'Niluva', 'Ninla', 'Nirelia', 'Nivama', 'Nivene', 'Nodryn', 'Norasa', 'Noreni', 'Nothas', 'Nudryn', 'Nulwrila', 'Nurara', 
'Nurisea', 'Nurona', 'Nurvyna', 'Nusana', 'Nuula', 'Odesa', 'Odrasa', 'Odrys', 'Odyna', 'Olvyia', 'Orama', 'Orani', 'Orara', 
'Orea', 'Orona', 'Orvana', 'Oryla', 'Qyss', 'Radene', 'Radrase', 'Rala', 'Ralsynilsa', 'Ramavel', 'Rami', 'Ramila', 'Ramu', 
'Rana', 'Rania', 'Ranis', 'Ranyna', 'Rarili', 'Rarusi', 'Ravania', 'Ravel', 'Ravela', 'Ravila', 'Raynil', 'Raynila', 'Rela', 
'Reldsii', 'Relenila', 'Relmerea', 'Relmeria', 'Rena', 'Rendrasa', 'Renkathi', 'Rernel', 'Reron', 'Resetta', 'Revisii', 'Rianor', 
'Ridinna', 'Riinsi', 'Rila', 'Rinori', 'Riray', 'Rironi', 'Ris', 'Risa', 'Rudrasa', 'Rurvyn', 'Ruvali', 'Ryna', 'Saalu', 'Sadelia', 
'Salima', 'Salina', 'Salori', 'Salver', 'Saly', 'Samtri', 'Sanas', 'Satha', 'Sathdira', 'Sathryn', 'Sava', 'Savi', 'Savila', 'Savile', 
'Sayla', 'Sayne', 'Sedura', 'Sehlena', 'Sela', 'Selvura', 'Sem', 'Semoa', 'Sen', 'Sena', 'Serana', 'Seritath', 'Servyna', 'Seryna', 
'Seryne', 'Sethan', 'Sethisa', 'Sevame', 'Sevy', 'Seyne', 'Seyrena', 'Shelethys', 'Shiralas', 'Shra', 'Sia', 'Siid', 'Siila', 'Silen', 
'Sirari', 'Sirili', 'Sirilu', 'Sivisia', 'Sodra', 'Solryn', 'Sorosi', 'Sovi', 'Suldrini', 'Surii', 'Suronii', 'Sursi', 'Taderi', 'Taelu', 
'Talama', 'Talamu', 'Talari', 'Talmeni', 'Talsi', 'Talsyne', 'Taluri', 'Talvini', 'Tama', 'Tamira', 'Tanar', 'Tanisa', 'Tarania', 
'Tarvili', 'Tavya', 'Tedas', 'Tedoran', 'Telare', 'Teldyni', 'Teleri', 'Telura', 'Tenara', 'Tendren', 'Teranya', 'Ternu', 'Tereri', 
'Teroni', 'Tevynni', 'Thelama', 'Thelvamu', 'Thera', 'Therana', 'Thilse', 'Tifosi', 'Tildsi', 'Tilenra', 'Tilore', 'Tivela', 
'Tirvina', 'Tonas', 'Tovisa', 'Traldrisa', 'Trayna', 'Trayniria', 'Tredare', 'Tredere', 'Tremona', 'Udrasi', 'Ulene', 'Urada', 
'Urava', 'Uravasa', 'Ureso', 'Urila', 'Urili', 'Urona', 'Urrila', 'Uryne', 'Uthisii', 'Vadramea', 'Vadusa', 'Vadyne', 'Vala', 
'Valana', 'Valesu', 'Valvesu', 'Valyia', 'Valyn', 'Vamoni', 'Varasa', 'Varila', 'Varona', 'Varoni', 'Vaveli', 'Vayne', 'Vedelea', 
'Vedyne', 'Velanda', 'Velas', 'Veldrana', 'Velsa', 'Venae', 'Venoni', 'Veran', 'Veranim', 'Verilu', 'Vermethys', 'Veru', 'Vess', 
'Vethisa', 'Veya', 'Vila', 'Vilrani', 'Vim', 'Vindamea', 'Vinden', 'Visthina', 'Vivyne', 'Vlaasti', 'Vlesyl', 'Voldsea', 'Volene', 
'Volmyni', 'Volyn', 'Vrali', 'Vuri', 'Vurila', 'Wren', 'Xand', 'Zaristesi'
]


###############################################################################
# Markov Name model
# A random name generator, by Peter Corbett
# http://www.pick.ucam.org/~ptc24/mchain.html
# This script is hereby entered into the public domain
###############################################################################
class Mdict:
    def __init__(self):
        self.d = {}
    def __getitem__(self, key):
        if key in self.d:
            return self.d[key]
        else:
            raise KeyError(key)
    def add_key(self, prefix, suffix):
        if prefix in self.d:
            self.d[prefix].append(suffix)
        else:
            self.d[prefix] = [suffix]
    def get_suffix(self,prefix):
        l = self[prefix]
        return random.choice(l)  

class NameGenerator:
    """
    A name from a Markov chain
    """
    def __init__(self, names, chainlen = 2):
        """
        Building the dictionary
        """
        if chainlen > 10 or chainlen < 1:
            print "Chain length must be between 1 and 10, inclusive"
            sys.exit(0)
    
        self.mcd = Mdict()
        oldnames = []
        self.chainlen = chainlen
    
        for l in names:
            l = l.strip()
            oldnames.append(l)
            s = " " * chainlen + l
            for n in range(0,len(l)):
                self.mcd.add_key(s[n:n+chainlen], s[n+chainlen])
            self.mcd.add_key(s[len(l):len(l)+chainlen], "\n")

        self.generated = []
        self.names = names
 
    def new(self):
        """
        New name from the Markov chain
        """
        prefix = " " * self.chainlen
        name = ""
        suffix = ""
        while True:
            suffix = self.mcd.get_suffix(prefix)
            if suffix == "\n" or len(name) > 9:
                break
            else:
                name = name + suffix
                prefix = prefix[1:] + suffix
        return name.capitalize()

    def generate(self):
        while True:
            name = self.new()
            if not name in self.names and not name in self.generated:
                self.generated.append(name)
                return name

if __name__ == '__main__':
    import sys

    generator = NameGenerator(females)
    sys.stdout.writelines(('FEMALES', '\n', '-------', '\n'))
    for i in range(100):
        sys.stdout.write(generator.generate() + (', ' if i != 99 else ''))
        if (i + 1) % 10 == 0: sys.stdout.write('\n')
    sys.stdout.write('\n')

    generator = NameGenerator(males)
    sys.stdout.writelines(('MALES', '\n', '-----', '\n'))
    for i in range(100):
        sys.stdout.write(generator.generate() + (', ' if i != 99 else ''))
        if (i + 1) % 10 == 0: sys.stdout.write('\n')
    sys.stdout.write('\n')

    generator = NameGenerator(females + males)
    sys.stdout.writelines(('UNISEX', '\n', '------', '\n'))
    for i in range(100):
        sys.stdout.write(generator.generate() + (', ' if i != 99 else ''))
        if (i + 1) % 10 == 0: sys.stdout.write('\n')
    sys.stdout.write('\n')

    sys.stdout.flush()
