-- Message de fin quête 1 Menace intérieure
insert into world.quest_offer_reward_locale (ID, locale, RewardText, VerifiedBuild) values (783, 'frFR', 'Ah, parfait, un autre volontaire. Il y en a beaucoup qui se présentent comme vous, en ce moment. $B$BJ''espère que nous serons assez nombreux.$B$BLes terres humaines sont menacées de l''extérieur et nos principales forces sont rassemblées loin d''ici. En conséquence, des bandes de hors-la-loi corrompus prospèrent maintenant dans le pays.$B$BNous aurons à combattre sur tous les fronts, $N. Préparez vous à une longue campagne.',19091);

--La première quête disait 6 alors que le compteur demande 8
update world.quest_template_locale set Objectives = 'Tuez 8 Vermines kobolds, puis revenez voir le Maréchal McBride' where locale = 'frFR' and ID = 7;

-- Message de fin menace
insert into world.quest_offer_reward_locale (ID, locale, RewardText, VerifiedBuild) values (7, 'frFR', 'Bien. Ces kobolds sont des voleurs et des lâches, mais en grand nombre ils deviennent dangereux. Et les humains de Hurlevent n''ont pas besoin d''une menace de plus.$B$BVous avez toute ma gratitude pour les avoir détruits.',19091);

--pas de traduction du message intermédiaire
insert into world.quest_request_items_locale (ID, locale, CompletionText, VerifiedBuild) values (7, 'frFR', 'Comment se passe la chasse, $N ? Avez-vous trouvé et exterminé ces vermines ?', 19091);

-- Message de fin quête des loups
insert into world.quest_offer_reward_locale (ID, locale, RewardText, VerifiedBuild) values (5261, 'frFR', 'C''est vrai. Je recherche quelqu''un qui pourrait chasser des loups pour moi ! Êtes-vous cette personne ?',19091);

-- intermédiaire quetes loup
insert into world.quest_request_items_locale (ID, locale, CompletionText, VerifiedBuild) values (33, 'frFR', 'Hé, $N. Comment se passe la chasse des loups malades ?', 19091);

-- fin quetes loup
insert into world.quest_offer_reward_locale (ID, locale, RewardText, VerifiedBuild) values (33, 'frFR', 'C''était une tâche sinistre mon ami, mais vous avez respecté votre part du contrat.$B$BJ''ai quelques trucs qui pourraient vous servir. Faites votre choix !', 19091);
