# -*- coding: utf-8 -*-
DATA = [
    {
        'code': 'alphabet-secret',
        'name': 'Alphabet secret (variable)',
        'type': 'advanced',
        'attribute': 'intelligence',
        'description': 'Cette compétence permet de lire et de rédiger des messages secrets. Il existe plusieurs codes secrets utilisés dans l’Empire. Les alphabets secrets ne sont pas très sophistiqués et servent essentiellement à signaler un danger, désigner une cible, marquer une personne protégée, etc. Aucun test de compétence n’est requis pour déchiffrer des messages de base, mais le MJ peut en exiger pour déchiffrer des messages complexes ou dont les signes sont un peu effacés ou abîmés. À l’instar de Connaissances académiques,Alphabet secret n’est pas une compétence unique mais multiple. Les alphabets secrets les plus répandus sont les suivants : l’alphabet des pisteurs, l’alphabet des rôdeurs, l’alphabet des templiers et l’alphabet des voleurs.',
        'linked_talents': '',
        'declinations': [
            ('pisteur', 'Pisteurs'),
            ('rodeur', 'Rôdeurs'),
            ('templier', 'Templiers'),
            ('voleur', 'Voleurs'),
        ],
    },
    {
        'code': 'baratin',
        'name': 'Baratin',
        'type': 'advanced',
        'attribute': 'sociability',
        'description': 'On utilise cette compétence pour gagner du temps en baratinant un interlocuteur. Le discours tenu par le baratineur n’est jamais rationnel (sinon, on utiliserait plutôt Charisme) puisqu’il ne cherche qu’à dérouter son interlocuteur.Les victimes d’un test de Baratin couronné de succès ont droit à un test de Force Mentale pour percer la ruse à jour. En cas d’échec, elles ne peuvent rien faire pendant un round, en restent bouche bée et abasourdies, se demandant si leur interlocuteur est ivre, fou ou les deux à la fois. On ne peut pas utiliser Baratin si les cibles se livrent à un combat ou sont menacées par un danger immédiat. La compétence permet d’affecter une personne par tranche de 10 points en Sociabilité. Cependant, les victimes doivent comprendre la langue parlée par le baratineur pour que la compétence fonctionne.',
        'linked_talents': '',
    },
    {
        'code': 'braconnage',
        'name': 'Braconnage',
        'type': 'advanced',
        'attribute': 'agility',
        'description': 'Cette compétence permet de poser des pièges et d’appâter afin d’attraper divers animaux. Les pièges destinés à immobiliser et à tuer sont répandus dans l’Empire. On fait un test de compétence par jour et par piège.Un succès indique qu’une créature a été capturée.',
        'linked_talents': '',
    },
    {
        'code': 'canotage',
        'name': 'Canotage',
        'type': 'base',
        'attribute': 'strength',
        'description': 'On utilise cette compétence pour ramer et diriger une barque, un canot, une embarcation à fond plat et tout bateau similaire. Ramer dans des conditions normales ne requiert aucun test de compétence. Cependant,le MJ peut exiger des tests dans des conditions climatiques difficiles et dans des eaux agitées ou parsemées d’obstacles.',
        'linked_talents': '',
    },
    {
        'code': 'charisme',
        'name': 'Charisme',
        'type': 'base.',
        'attribute': 'sociability',
        'description': 'cette compétence permet de manipuler autrui. Les tests de Charisme peuvent être utilisés pour amener des individus ou de petits groupes de personnes à changer d’avis, pour mentir de manière convaincante, pour bluffer et même mendier. Les insinuations et la séduction dépendent aussi de la compétence Charisme. Les tests de compétence qui visent à convaincre autrui de faire quelque chose d’inhabituel ou allant à l’encontre de sa nature donnent droit à un test de FM pour y résister. La compétence permet d’affecter une personne par tranche de 10 points en Sociabilité. Cependant, les victimes doivent comprendre la langue parlée par l’utilisateur pour que la compétence fonctionne.',
        'linked_talents': ['code-de-la-rue', 'eloquence', 'etiquette', 'intrigant','orateur-ne'],
    },
    {
        'code': 'commandement',
        'name': 'Commandement',
        'type': 'base',
        'attribute': 'sociability',
        'description': 'On utilise cette compétence pour amener des subalternes à exécuter des ordres. Quand le test de compétence est couronné de succès, les ordres sont exécutés tels qu’ils ont été donnés. En cas d’échec, les ordres sont mal interprétés ou les subalternes ne font rien du tout (au choix du MJ). La compétence Commandement ne permet pas de donner des ordres à de parfaits étrangers, mais uniquement à ceux qui sont déjà placés sous l’autorité de son utilisateur.',
        'linked_talents': '',
    },
    {
        'code': 'commerage',
        'name': 'Commérage',
        'type': 'base',
        'attribute': 'sociability',
        'description': 'Cette compétence permet d’obtenir des informations. Elle est utile pour avoir vent des rumeurs et des dernières nouvelles, mais également pour engager une conversation des plus anodines.',
        'linked_talents': ['code-de-la-rue', 'etiquette'],
    },
    {
        'code': 'conduite-dattelages',
        'name': 'Conduite d’attelages',
        'type': 'base',
        'attribute': 'strength',
        'description': 'On utilise cette compétence pour conduire des carrioles et des chariots, voire des chars. Conduire un attelage dans des conditions normales ne requiert pas de test. Cependant, des tests peuvent être nécessaires en terrain difficile, à une vitesse excessive ou lors de manoeuvres dangereuses.',
        'linked_talents': '',
    },
    {
        'code': 'connaissances-academiques',
        'name': 'Connaissances académiques (variable)',
        'declinations': [
            ('arts', 'Arts'),
            ('astronomie', 'Astronomie'),
            ('demonologie', 'Démonologie'),
            ('droit', 'Droit'),
            ('histoire', 'Histoire'),
            ('ingenierie', 'Ingénierie'),
            ('genealogie-heraldique', 'Généalogie/Héraldique'),
            ('magie', 'Magie'),
            ('necromancie', 'Nécromancie'),
            ('philosophie', 'Philosophie'),
            ('runes', 'Runes'),
            ('science', 'Science'),
            ('strategie-tactique', 'Stratégie/Tactique'),
            ('theologie', 'Théologie'),
        ],
        'type': 'advanced',
        'attribute': 'intelligence',
        'description': 'On utilise la compétence Connaissances académiques pour se souvenir de faits et de chiffres et (si on dispose des archives adéquates) pour effectuer des recherches. Elle représente un savoir beaucoup plus approfondi que Connaissances générales et nécessite de longues études. La compétence Connaissances académiques est particulière dans le sens où elle n’est pas unique mais multiple. En effet, il existe une multitude de compétences Connaissances académiques distinctes qu’il faut acquérir séparément. Chaque compétence Connaissances académiques représente un domaine particulier, indiqué entre parenthèses. Par exemple, la compétence Connaissances académiques (religion) est différente de Connaissances académiques (histoire). Les connaissances les plus répandues concernent les domaines suivants : arts, astronomie, démonologie, droit, histoire, ingénierie, généalogie/héraldique, magie, nécromancie, philosophie, runes, science, stratégie/tactique, théologie.',
        'linked_talents': '',
    },
    {
        'code': '',
        'name': 'Connaissances générales (variable)',
        'declinations': [
            ('bretonnie', 'Bretonnie'),
            ('elfes', 'Elfes'),
            ('empire', 'Empire'),
            ('estalie', 'Estalie'),
            ('halflings', 'Halflings'),
            ('kislev', 'Kislev'),
            ('nains', 'Nains'),
            ('norsca', 'Norsca'),
            ('ogres', 'Ogres'),
            ('pays-perdu', 'Pays Perdu'),
            ('principautes-frontalieres', 'Principautés frontalières'),
            ('tilee', 'Tilée'),
        ],
        'type': 'advanced',
        'attribute': 'intelligence',
        'description': 'La compétence Connaissances générales permet de se souvenir des coutumes, des institutions, des traditions, des personnalités et des superstitions d’une nation, d’une race ou d’un groupe culturel particulier. Connaissances générales ne représente pas un savoir étudié de manière formelle (c’est le domaine de Connaissances académiques), mais une expérience apprise sur le tas, en grandissant ou en voyageant longtemps dans une région donnée. Comme Connaissances académiques, Connaissances générales n’est pas une compétence unique mais multiple. Les domaines de Connaissances générales les plus répandus sont : Bretonnie, elfes, Empire, Estalie, halflings, Kislev, nains, Norsca, ogres, Pays Perdu, Principautés Frontalières et Tilée.',
        'linked_talents': ['grand-voyageur'],
    },
    {
        'code': 'crochetage',
        'name': 'Crochetage',
        'type': 'advanced',
        'attribute': 'agility',
        'description': 'On utilise cette compétence pour déverrouiller des serrures. En temps normal, un test couronné de succès permet de crocheter une serrure, mais le MJ peut en exiger plusieurs s’il s’agit de mécanismes particulièrement complexes. Cette compétence peut également être utilisée pour désamorcer des pièges mécaniques.',
        'linked_talents': ['connaissance-des-pieges'],
    },
    {
        'code': 'deguisement',
        'name': 'Déguisement',
        'type': 'base',
        'attribute': 'sociability',
        'description': 'On utilise cette compétence pour masquer sa véritable apparence.Vêtements,accessoires et maquillage sont souvent la clef d’un déguisement réussi. Il est également possible de se faire passer pour un membre du sexe opposé, d’une autre race ou pour une personne précise, mais la tâche est bien plus ardue. Le test de Déguisement est souvent opposé à un test de Perception de la part de l’adversaire.',
        'linked_talents': ['imitation'],
    },
    {
        'code': 'deplacement-silencieux',
        'name': 'Déplacement silencieux',
        'type': 'base',
        'attribute': 'agility',
        'description': 'Cette compétence est utilisée pour se déplacer discrètement. Un personnage utilisant cette compétence ne peut faire qu’une action de mouvement au cours d’un round. Le test de Déplacement silencieux est souvent opposé à un test de Perception de l’adversaire.',
        'linked_talents': ['camouflage-rural', 'camouflage-souterrain', 'camouflage-urbain'],
    },
    {
        'code': 'dissimulation',
        'name': 'Dissimulation',
        'type': 'base',
        'attribute': 'agility',
        'description': 'On utilise cette compétence pour se cacher de ses ennemis. Il est indispensable que le terrain présente un endroit où se cacher (des arbres, des murs, un bâtiment, etc.). Dans le cas contraire, le test de compétence échoue automatiquement (impossible de se cacher en plein milieu d’une rue vide !). Le test de Dissimulation est souvent opposé à un test de Perception de la part de l’adversaire.',
        'linked_talents': ['camouflage-rural', 'camouflage-souterrain', 'camouflage-urbain'],
    },
    {
        'code': 'dressage',
        'name': 'Dressage',
        'type': 'advanced',
        'attribute': 'sociability',
        'description': 'On utilise cette compétence pour entraîner les animaux à faire des tours et à obéir à des ordres simples. En général, on dresse surtout les chiens, les chevaux et les faucons, bien qu’il soit possible de former des animaux moins courants si le MJ le permet. Dresser correctement un animal prend du temps. On effectue un test de compétence par semaine durant la période de dressage.Apprendre un tour simple ne requiert qu’un test réussi.Une tâche moyennement difficile en nécessite trois et une tâche difficile peut être apprise après dix tests réussis.',
        'linked_talents': '',
    },
    {
        'code': 'emprise-sur-les-animaux',
        'name': 'Emprise sur les animaux',
        'type': 'advanced',
        'attribute': 'sociability',
        'description': 'Cette compétence permet de se lier d’amitié avec les animaux. Les animaux domestiques sont toujours amicaux à votre égard. Les animaux sauvages ou dressés à l’attaque (comme les chiens de guerre) peuvent être calmés via un test couronné de succès. Le MJ peut imposer des malus dans le cas d’animaux particulièrement loyaux ou têtus. Notez que cette compétence ne fonctionne pas avec les monstres.',
        'linked_talents': '',
    },
    {
        'code': 'equitation',
        'name': 'Équitation',
        'type': 'base',
        'attribute': 'agility',
        'description': 'Cette compétence est utilisée pour monter des chevaux et autres montures similaires. En temps normal, l’équitation ne nécessite pas de test de compétence. Cependant, le MJ peut exiger des tests de compétence pour galoper, faire la course, guider sa monture sur un terrain accidenté, sauter sur une monture en mouvement, etc.',
        'linked_talents': ['acrobatie-equestre'],
    },
    {
        'code': 'escalade',
        'name': 'Escalade',
        'type': 'base',
        'attribute': 'strength',
        'description': 'On utilise cette compétence pour escalader des clôtures, des murs et autres obstacles verticaux. Dans des conditions normales, un test de compétence est nécessaire à chaque round. L’utilisation de la compétence Escalade est une action complète et le personnage peut grimper d’un nombre de mètres égal à la moitié de sa caractéristique de Mouvement (arrondir à l’entier supérieur) quand il réussit un test.',
        'linked_talents': '',
    },
    {
        'code': 'escamotage',
        'name': 'Escamotage',
        'type': 'advanced',
        'attribute': 'agility',
        'description': 'On utilise cette compétence pour faire disparaître de petits objets dans la paume de la main, pour faire les poches de quelqu’un ou réaliser des tours de passe-passe avec des pièces ou des cartes. Le test d’Escamotage est souvent opposé à un test de Perception de l’observateur.',
        'linked_talents': '',
    },
    {
        'code': 'esquive',
        'name': 'Esquive',
        'type': 'advanced',
        'attribute': 'agility',
        'description': 'Cette compétence permet d’éviter les attaques au combat au corps à corps. On peut utiliser l’Esquive une fois par round. Voir le Chapitre 6 : Combat, dégâts et mouvements.',
        'linked_talents': '',
    },
    {
        'code': 'evaluation',
        'name': 'Évaluation',
        'type': 'base',
        'attribute': 'intelligence',
        'description': 'Cette compétence permet de déterminer la valeur d’objets courants et de biens précieux comme les bijoux, les gemmes et les oeuvres d’art. Un test de compétence couronné de succès permet de connaître le prix de vente de l’objet. Dans la mesure où un échec peut conduire à une évaluation erronée, il vaut mieux que le MJ jette les dés du test d’Évaluation en secret et qu’il indique au joueur ce que son personnage croit être le prix de l’objet.',
        'linked_talents': ['dur-en-affaires', 'talent-artistique'],
    },
    {
        'code': 'expression-artistique',
        'name': 'Expression artistique (variable)',
        'type': 'advanced',
        'declinations': [
            ('acrobate', 'Acrobate'),
            ('acteur', 'Acteur'),
            ('bouffon', 'Bouffon'),
            ('chanteur', 'Chanteur'),
            ('chiromancien', 'Chiromancien'),
            ('clown', 'Clown'),
            ('comedien', 'Comédien'),
            ('conteur', 'Conteur'),
            ('cracheur-de-feu', 'Cracheur de feu'),
            ('danseur', 'Danseur'),
            ('jongleur', 'Jongleur'),
            ('mime', 'Mime'),
            ('musicien', 'Musicien'),
        ],
        'attribute': 'sociability',
        'description': 'On utilise cette compétence pour divertir un groupe de spectateurs.Comme Connaissances académiques,Expression artistique est une compétence multiple. Les domaines les plus répandus pour cette compétence sont : acrobate, acteur, bouffon, chanteur, chiromancien, clown, comédien, conteur, cracheur de feu, danseur, jongleur, mime et musicien.',
        'linked_talents': ['contorsionniste', 'imitation'],
    },
    {
        'code': 'filature',
        'name': 'Filature',
        'type': 'advanced',
        'attribute': 'agility',
        'description': 'Cette compétence permet de suivre autrui sans être vu. La Filature est souvent opposé à la Perception de l’adversaire.',
        'linked_talents' : '',
    },
    {
        'code': 'focalisation',
        'name': 'Focalisation',
        'type': 'advanced',
        'attribute': 'mental_strength',
        'description': 'On utilise cette compétence pour contrôler les vents de magie.Tous les sorts nécessitent la manipulation de ces vents de magie, mais la compétence Focalisation est utilisée quand on a besoin d’une plus grande précision ou d’une meilleure maîtrise. Pour plus de détails concernant les sorts et le rôle de la compétence Focalisation, reportez vous au Chapitre 7 : La magie.',
        'linked_talents': ['harmonie-aethyrique'],
    },
    {
        'code': 'fouille',
        'name': 'Fouille',
        'type': 'base',
        'attribute': 'intelligence',
        'description': 'On utilise cette compétence pour rechercher des indices, des trésors et autres objets cachés (y compris des pièges) dans un lieu donné. Un test est nécessaire pour chaque pièce ou zone.',
        'linked_talents': '',
    },
    {
        'code': 'hypnotisme',
        'name': 'Hypnotisme',
        'type': 'advanced',
        'attribute': 'mental_strength',
        'description': 'Cette compétence permet de mettre autrui en état de transe. Il faut conserver l’attention du sujet pendant une minute (souvent en captant son regard à l’aide d’un pendule et/ou en psalmodiant), après laquelle l’utilisateur doit réussir un test d’Hypnotisme. Un sujet non consentant peut résister au moyen d’un test de Force Mentale. Une fois le sujet rentré en transe, l’utilisateur peut lui poser une question par tranche de 10 points dont il dispose en Force Mentale.Les réponses doivent être sincères. Remarquez que le sujet répond ce qu’il croit être vrai et qu’il peut très bien se tromper. Une fois la dernière question posée, le sujet sort de la transe.',
        'linked_talents': '',
    },
    {
        'code': 'intimidation',
        'name': 'Intimidation',
        'type': 'base',
        'attribute': 'strength',
        'description': 'Cette compétence permet d’exercer des pressions sur un individu ou de l’effrayer. Les victimes de l’Intimidation peuvent résister en réussissant un test de Force Mentale. La façon dont les PNJ réagissent à l’Intimidation dépend entièrement du MJ, qui la détermine en fonction de leur personnalité et du résultat du test. Dans certaines circonstances (chantage, etc.),le MJ peut permettre au joueur d’effectuer un test d’Intimidation à l’aide de sa Sociabilité plutôt qu’avec sa Force.',
        'linked_talents': ['menacant'],
    },
    {
        'code': 'jeu',
        'name': 'Jeu',
        'type': 'base',
        'attribute': 'intelligence',
        'description': 'On utilise cette compétence pour jouer aux jeux de hasard, comme les jeux de dés et de cartes. Chaque participant mise la même somme et chacun effectue un test de Jeu opposé. Celui qui l’emporte ramasse la cagnotte. Le joueur peut très bien décider de perdre volontairement, auquel cas son personnage perd automatiquement.',
        'linked_talents': ['calcul-mental'],
    },
    {
        'code': 'language-mystique',
        'name': 'Langage mystique',
        'type': 'advanced',
        'declinations': [
            ('demonik', 'Demonik'),
            ('elfique-mystique', 'Elfique mystique'),
            ('magick', 'Magick'),
        ],
        'attribute': 'intelligence',
        'description': 'On utilise cette compétence pour lancer des sorts. Votre personnage doit parler un langage mystique s’il veut utiliser la magie. Contrairement aux autres langues, les langages mystiques ne servent pas à tenir une conversation, mais à manipuler des énergies magiques. Tous les parchemins et les grimoires sont rédigés en langage mystique. À l’instar de Connaissances académiques, Langage mystique n’est pas une compétence unique mais multiple. Les langages mystiques les plus répandus sont les suivants : le demonik (aussi appelée lingua daemonica par les magisters impériaux), l’elfique mystique et le magick (aussi appelée lingua praestentia).',
        'linked_talents': '',
    },
    {
        'code': 'langage-secret',
        'name': 'Langage secret (variable)',
        'type': 'advanced',
        'declinations': [
            ('bataille', 'Bataille'),
            ('guilde', 'Guilde'),
            ('rodeurs', 'Rôdeurs'),
            ('voleurs', 'Voleurs'),
        ],
        'attribute': 'intelligence',
        'description': 'Cette compétence est utilisée pour communiquer secrètement entre individus pratiquant la même profession. Les langages secrets s’apparentent plus à des codes qu’à de véritables langues. En utilisant certains signifiants, qu’il s’agisse de gestes ou de mots codés, l’utilisateur peut s’exprimer dans une langue tout en utilisant un code d’expression qui donne un sens plus profond à ses paroles ou qui transmet rapidement une grande quantité d’informations. En temps normal, aucun test n’est nécessaire si tous les interlocuteurs connaissent le même langage secret. Le MJ peut exiger des tests si les conditions sont défavorables (lieu bruyant,tumulte d’une bataille, etc.). À l’instar de Connaissances académiques,Langage secret n’est pas une compétence unique, mais multiple. Les langages secrets les plus répandus sont : le langage de bataille, le langage de guilde, le langage des rôdeurs et le langage des voleurs.',
        'linked_talents': '',
    },
    {
        'code': 'langue',
        'name': 'Langue (variable)',
        'type': 'advanced',
        'declinations': [
            ('bretonnien', 'Bretonnien'),
            ('classique', 'Classique'),
            ('eltharin', 'Eltharin (elfes)'),
            ('estalien', 'Estalien'),
            ('halfling', 'Halfling'),
            ('khazalid', 'Khazalid (nains)'),
            ('kislevien', 'Kislevien'),
            ('norse', 'Norse (Norsca)'),
            ('reikspiel', 'Reikspiel (Empire)'),
            ('tileen', 'Tiléen'),
            ('gobelinoide', 'Gobelinoïde'),
            ('grumbarth', 'Grumbarth (Ogres)'),
            ('sombre', 'Sombre (hommes-bêtes, Chaos)'),
        ],
        'attribute': 'intelligence',
        'description': 'Cette compétence permet à deux individus de communiquer par l’intermédiaire d’une langue qu’ils parlent l’un et l’autre. La plupart des langues parlées dans le Vieux Monde dérivent d’une racine commune, mais celle-ci a été si profondément modifiée que quasiment chaque race ou nation parle désormais son propre langage. En temps normal, aucun test de compétence n’est requis si tous les interlocuteurs connaissent la même langue. Un test peut être nécessaire si le personnage tente d’imiter ou de comprendre un accent ou un patois régional ou s’il désire se faire passer pour un autochtone d’un certain pays s’il ne s’agit pas de sa langue d’origine. À l’instar de Connaissances académiques, Langue n’est pas une compétence unique mais multiple. Les langues les plus répandues et les peuples ou les pays où on les pratique sont les suivants : le bretonnien (Bretonnie), l’eltharin (elfes), l’estalien (Estalie), le halfling (halflings), le khazalid (nains), le kislevien (Kislev), le norse (Norsca), le reikspiel (Empire) et le tiléen (Tilée). Il existe une autre langue, la langue classique,un ancien langage qui a la faveur des érudits, mais que l’on parle fort peu aujourd’hui. Parmi les langues moins civilisées, on peut aussi citer : le gobelinoïde (gobelins,hobgobelins, orques), le grumbarth (ogres) et le langage sombre (hommes-bêtes, Chaos).',
        'linked_talents': ['grand-voyageur', 'imitation', 'linguistique'],
    },
    {
        'code': 'lecture-sur-les-levres',
        'name': 'Lecture sur les lèvres',
        'type': 'advanced',
        'attribute': 'intelligence',
        'description': 'Cette compétence permet de capter des conversations qui se situent hors de portée de l’ouïe. L’utilisateur doit cependant voir clairement la partie inférieure du visage des interlocuteurs et comprendre la langue qu’ils utilisent.',
        'linked_talents': ['acuite-visuelle'],
    },
    {
        'code': 'lire-ecrire',
        'name': 'Lire/écrire',
        'type': 'advanced',
        'attribute': 'intelligence',
        'description': 'Cette compétence vous permet de lire et d’écrire toutes les langues que vous parlez. En temps normal, lire ou écrire ne nécessite aucun test de compétence. Un test peut toutefois être nécessaire pour déchiffrer des tournures de phrase obscures ou archaïques ou des idiomes peu répandus.',
        'linked_talents': ['linguistique'],
    },
    {
        'code': 'marchandage',
        'name': 'Marchandage',
        'type': 'base',
        'attribute': 'sociability',
        'description': 'On utilise cette compétence pour négocier des prix et des échanges.Dans le cadre de la vie quotidienne,pour négocier les prix des denrées au marché par exemple, un simple test de compétence suffit.Toutefois, dans le cas d’échanges importants (comme la négociation du prix d’un manuscrit rare), le MJ peut exiger des tests de compétence opposés, utilisant le Marchandage des deux parties en présence.',
        'linked_talents': ['dur-en-affaires'],
    },
    {
        'code': 'metier',
        'name': 'Métier (variable)',
        'type': 'advanced',
        'declinations': [
            ('apothicaire', 'Apothicaire (Int)'),
            ('arquebusier', 'Arquebusier (Ag)'),
            ('artiste', 'Artiste (Ag)'),
            ('brasseur', 'Brasseur (Int)'),
            ('calligraphe', 'Calligraphe (Ag)'),
            ('cartographe', 'Cartographe (Ag)'),
            ('charpentier', 'Charpentier (Ag)'),
            ('charpentier-naval', 'Charpentier naval (Int)'),
            ('cordonnier', 'Cordonnier (Ag)'),
            ('cristallier', 'Cristallier (Ag)'),
            ('cuisinier', 'Cuisinier (Int)'),
            ('embaumeur', 'Embaumeur (Int)'),
            ('fabricant-darcs', 'Fabricant d\'arcs (Ag)'),
            ('fabricant-darmes', 'Fabricant d\'armes (F)'),
            ('fabricant-darmures', 'Fabricant d\'armures (F)'),
            ('fabricant-de-bougies', 'Fabricant de bougies (Ag)'),
            ('fermier', 'Fermier (F)'),
            ('forgeron', 'Forgeron (F)'),
            ('herboriste', 'Herboriste (Int)'),
            ('macon', 'Maçon (Ag)'),
            ('marchand', 'Marchand (Soc)'),
            ('meunier', 'Meunier (F)'),
            ('mineur', 'Mineur (F)'),
            ('orfevre', 'Orfèvre (Ag)'),
            ('prospecteur', 'Prospecteur (F)'),
            ('tailleur', 'Tailleur (Ag)'),
            ('tanneur', 'Tanneur (F)'),
            ('tonnelier', 'Tonnelier (F)'),
        ],
        'attribute': 'variable',
        'description': 'Cette compétence permet de pratiquer un métier. À l’instar de Connaissances académiques, cette compétence n’est pas unique mais multiple. Les métiers les plus répandus et les caractéristiques qui leur sont associées sont les suivants : apothicaire (Int), arquebusier (Ag), artiste (Ag), brasseur (Int), calligraphe (Ag), cartographe (Ag), charpentier (Ag),charpentier naval (Int),cordonnier (Ag),cristallier (Ag), cuisinier (Int), embaumeur (Int), fabricant d’arcs (Ag), fabricant d’armes (F), fabricant d’armures (F), fabricant de bougies (Ag), fermier (F), forgeron (F),herboriste (Int),maçon (Ag),marchand (Soc),meunier (F),mineur (F), orfèvre (Ag), prospecteur (F), tailleur (Ag), tanneur (F) et tonnelier (F).',
        'linked_talents': ['savoir-faire-nain', 'talent-artistique'],
    },
    {
        'code': 'natation',
        'name': 'Natation',
        'type': 'base',
        'attribute': 'strength',
        'description': 'Cette compétence permet de nager et de plonger. Nager dans des conditions normales ne requiert aucun test de compétence. Le MJ peut en demander un quand l’eau est particulièrement agitée ou quand il s’agit de nager pendant une longue période. La caractéristique de Mouvement du personnage est divisée par deux (arrondir à l’entier supérieur) quand il nage.',
        'linked_talents': '',
    },
    {
        'code': 'navigation',
        'name': 'Navigation',
        'type': 'advanced',
        'attribute': 'agility',
        'description': 'Cette compétence permet de manoeuvrer des bateaux à voiles. Ceux qui en disposent sont familiarisés avec les diverses tâches que l’on accomplit sur un bateau, la connaissance des divers types de voiles, la conduite à adopter par mauvais temps, etc.Naviguer en temps normal ne requiert pas de test de compétence. Cependant, le MJ peut exiger des tests dans des conditions climatiques difficiles et dans des eaux agitées ou parsemées d’obstacles.',
        'linked_talents': '',
    },
    {
        'code': 'orientation',
        'name': 'Orientation',
        'type': 'advanced',
        'attribute': 'intelligence',
        'description': 'On utilise cette compétence pour trouver son chemin, sur terre comme sur l’eau.Pour ce faire, on se sert des étoiles, des cartes et d’un bon sens de l’orientation. L’utilisateur peut également estimer la durée d’un voyage en fonction du terrain, de l’époque de l’année et du climat. En temps normal, un test réussi par jour permet de rester dans la bonne direction, mais le MJ peut exiger d’autres tests en cas de circonstances particulières.',
        'linked_talents': ['calcul-mental', 'sens-de-lorientation'],
    },
    {
        'code': 'perception',
        'name': 'Perception',
        'type': 'base',
        'attribute': 'intelligence',
        'description': 'Cette compétence vous permet d’observer votre environnement pour y déceler des détails qui passeraient normalement inaperçus. Elle sert également à déceler les pièges, les fosses et autres dangers physiques. Bien qu’on l’utilise la plupart du temps pour déterminer ce que voit le personnage, la compétence Perception recouvre en réalité tous les sens. On peut donc aussi s’en servir pour écouter, sentir, toucher et goûter. Il s’agit de la compétence qu’on utilise le plus en opposition avec des compétences comme Déguisement, Déplacement silencieux et Dissimulation. Elle peut aussi être utilisée pour estimer des quantités, des distances, etc. Dans ce cas, un échec indique que les informations obtenues sont erronées.',
        'linked_talents': ['acuite-auditive', 'acuite-visuelle', 'calcul-mental', 'connaissance-des-pieges', 'sens-aiguises'],
    },
    {
        'code': 'pistage',
        'name': 'Pistage',
        'type': 'advanced',
        'attribute': 'intelligence',
        'description': 'Cette compétence permet de traquer une proie, animale ou autre. Suivre une piste évidente ne requiert aucun test de compétence et ne nécessite pas de ralentir l’allure.Toutefois, dans des circonstances difficiles, un test peut être exigé. L’utilisateur peut également effectuer des tests pour déterminer sa distance par rapport à ses proies, leur nombre ou leur type racial.',
        'linked_talents': '',
    },
    {
        'code': 'preparation-de-poisons',
        'name': 'Préparation de poisons',
        'type': 'advanced',
        'attribute': 'intelligence',
        'description': 'Cette compétence permet de préparer un poison. La compétence recouvre l’utilisation des poisons d’origine animale (venins),naturelle et chimique.Pour plus d’informations sur les poisons et leurs effets, reportez-vous au Chapitre 5 : L’équipement.',
        'linked_talents': '',
    },
    {
        'code': 'resistance-a-lalcool',
        'name': 'Résistance à l’alcool',
        'type': 'base',
        'attribute': 'constitution',
        'description': 'On utilise cette compétence pour résister aux effets de l’alcool. Les buveurs expérimentés peuvent développer une tolérance remarquable. On effectue un test de compétence après chaque verre. Pour plus de détails concernant l’alcool et ses effets, reportez-vous au Chapitre 5 : L’équipement.',
        'linked_talents': '',
    },
    {
        'code': 'sens-de-la-magie',
        'name': 'Sens de la magie',
        'type': 'advanced',
        'attribute': 'mental_strength',
        'description': 'Parfois qualifiée de « troisième oeil », cette compétence est utilisée pour détecter la présence de magie. Les sorciers en parlent comme des sixième, septième et huitième sens. Un test couronné de succès permet à l’utilisateur de déterminer si un objet, un lieu ou une personne est enchanté par magie. Cette compétence permet également de distinguer les vents de magie et donc de déterminer s’ils soufflent plus ou moins fort en un lieu donné. Pour plus d’informations, reportez-vous au Chapitre 7 : La magie.',
        'linked_talents': ['harmonie-aethyrique'],
    },
    {
        'code': 'soins',
        'name': 'Soins',
        'type': 'advanced',
        'attribute': 'intelligence',
        'description': 'Cette compétence permet de prodiguer des soins médicaux aux blessés. Un test de Soins couronné de succès redonne 1d10 points de Blessures à un personnage Légèrement blessé et 1 point de Blessures à un personnage Gravement blessé. Un personnage blessé ne peut recevoir de tels soins qu’une fois pendant ou après chaque rencontre (combat, piège, chute, etc.) où il a subi des Blessures. Le jour suivant, et une fois par jour par la suite, le personnage blessé peut bénéficier d’un autre test de Soins.Pour plus d’information sur les Blessures et leur guérison, reportez-vous au Chapitre 6 : Combat, dégâts et mouvements.',
        'linked_talents': ['chirurgie'],
    },
    {
        'code': 'soins-des-animaux',
        'name': 'Soins des Animaux',
        'type': 'base',
        'attribute': 'intelligence',
        'description': 'Cette compétence permet de prendre soin des animaux domestiques et des animaux de la ferme, comme les chevaux, les vaches, les porcs, les boeufs, etc. Les soigner et les nourrir au quotidien ne requiert pas de test de compétence. Les tests servent essentiellement à déceler des maladies ou des signes de gêne, ou dans des circonstances spéciales (préparer une monture pour une parade, par exemple).',
        'linked_talents': '',
    },
    {
        'code': 'survie',
        'name': 'Survie',
        'type': 'base',
        'attribute': 'intelligence',
        'description': 'Cette compétence permet de survivre dans la nature et de se livrer à des activités comme la pêche, la chasse, la confection d’un feu de camp, la recherche de nourriture comestible, la construction d’abris improvisés, etc.',
        'linked_talents': '',
    },
    {
        'code': 'torture',
        'name': 'Torture',
        'type': 'advanced',
        'attribute': 'sociability',
        'description': 'Cette compétence permet de soutirer des informations à un sujet réfractaire par différents moyens. La compétence recouvre à la fois la torture physique et mentale. Une victime peut résister à la torture en réussissant un test de Force Mentale opposé.',
        'linked_talents': ['menacant'],
    },
    {
        'code': 'ventriloquie',
        'name': 'Ventriloquie',
        'type': 'advanced',
        'attribute': 'sociability',
        'description': 'Cette compétence permet de parler sans ouvrir les lèvres. Des observateurs particulièrement vigilants auront droit à un test de Perception opposé, à la discrétion du MJ.',
        'linked_talents': '',
    },
]
