PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE `users` (`id` integer,`username` text,`password` text, `login_secret` text,PRIMARY KEY (`id`));
INSERT INTO users VALUES(1,'{{xuiUsername}}','{{xuiPassword}}','');
CREATE TABLE `settings` (`id` integer,`key` text,`value` text,PRIMARY KEY (`id`));
INSERT INTO settings VALUES(1,'secret','114514');
INSERT INTO settings VALUES(2,'webPort','{{xuiPort}}');
INSERT INTO settings VALUES(3,'webListen','');
INSERT INTO settings VALUES(4,'webCertFile','/root/.acme.sh/{{acmeDir}}/fullchain.cer');
INSERT INTO settings VALUES(5,'webKeyFile','/root/.acme.sh/{{acmeDir}}/{{domain}}.key');
INSERT INTO settings VALUES(6,'webBasePath','{{xuiPath}}');
COMMIT;

