# -*- coding: utf-8 -*-
DATA = [
    {
        'code': 'hunter',
        'name': 'Chasseur',
        'description': 'Bien que l’Empire soit loin des tribus qui le fondèrent il y a 2 500 ans, certaines choses n’ont pas vraiment changé depuis. Si les paysans cultivent une partie des terres, de vastes régions impériales sont encore couvertes de forêts ou tout simplement hostiles à l’agriculture. C’est sur ces terres que les Chasseurs et autres trappeurs prospèrent. Qu’il s’agisse de pièges ou de tirs bien placés, ils utilisent les mêmes techniques que leurs ancêtres pour capturer le gibier. Il est nécessaire de disposer d’un certain talent pour traquer un animal sauvage tout en évitant les sinistres créatures des bois. Vêtu de peaux et de fourrures, le Chasseur passe parfois pour un sauvage auprès des citadins, mais il se soucie rarement de ce qu’on pense de lui.',
        'cc': 0,
        'ct': 15,
        'strength': 0,
        'constitution': 5,
        'agility': 10,
        'intelligence': 5,
        'mental_strength': 0,
        'sociability': 0,
        'attacks': 0,
        'wounds': 3,
    },
    {
        'code': 'initiate',
        'name': 'Initié',
        'description': 'La religion occupe aujourd’hui une place secondaire dans le coeur de nombreux habitants du Vieux Monde, mais cela n’empêche pas de jeunes hommes et femmes de consacrer leur existence aux dieux. Pour devenir prêtre, il faut développer des trésors de dévouement et de discipline. Mais avant de pouvoir prétendre devenir prêtre, il faut avoir été un Initié. Des professeurs des plus stricts leur donnent une instruction rigoureuse, mais ils n’ont pas le droit de prêcher ou de conduire l’office avant d’être officiellement ordonnés. Leur instruction inclut littérature, calligraphie, étude des textes sacrés et art du sermon. Ils apprennent également les bases du maniement des armes pour être capables de défendre leur temple en cas de besoin.',
        'cc': 5,
        'ct': 5,
        'strength': 0,
        'constitution': 5,
        'agility': 0,
        'intelligence': 10,
        'mental_strength': 10,
        'sociability': 10,
        'attacks': 0,
        'wounds': 2,
    },
    {
        'code': 'student',
        'name': 'Étudiant',
        'description': 'Les grandes villes de l’Empire abritent un certain nombre d’universités. À l’instar de l’école impériale des ingénieurs, la plupart sont financées par l’État. La première université de l’Empire fut fondée à Nuln, ville aujourd’hui encore réputée pour ses institutions pédagogiques (et, ironie du sort, pour l’école impériale d’artillerie). Les Étudiants de l’Empire ont le choix entre de nombreux cours, de l’histoire à l’anatomie en passant par la science. Évidemment, beaucoup préfèrent s’amuser avec leurs camarades dans les tavernes aux alentours de l’université et se font recaler en moins d’un an. Les Étudiants elfes ne se rendent pas aux universités impériales mais apprennent auprès de leurs propres maîtres. Les Étudiants halflings sont tolérés dans les universités en raison d’une obscure ordonnance impériale demandée par l’Ancien du Moot il y a bien longtemps de cela.',
        'cc': 0,
        'ct': 0,
        'strength': 0,
        'constitution': 0,
        'agility': 10,
        'intelligence': 10,
        'mental_strength': 5,
        'sociability': 10,
        'attacks': 0,
        'wounds': 2,
        'exits': ['initiate'],
        'talents': ['calcul-mental|grand-voyageur', 'etiquette|linguistique', 'intelligent|sociable']
    }
]
