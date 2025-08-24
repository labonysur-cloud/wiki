
CREATE DATABASE IF NOT EXISTS wiki_db;
USE wiki_db;


CREATE TABLE IF NOT EXISTS memory (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_text TEXT NOT NULL,
    wiki_response TEXT NOT NULL,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
);


CREATE TABLE IF NOT EXISTS timers (
    id INT AUTO_INCREMENT PRIMARY KEY,
    label VARCHAR(50) NOT NULL,          -- e.g., "pasta", "study"
    minutes INT NOT NULL,                 -- timer duration
    start_time DATETIME NOT NULL,         -- when timer was set
    status VARCHAR(20) DEFAULT 'active'  -- active, completed, canceled
);


CREATE TABLE IF NOT EXISTS user_preferences (
    id INT AUTO_INCREMENT PRIMARY KEY,
    key_name VARCHAR(50) NOT NULL,       -- e.g., "tts_voice"
    value VARCHAR(100) NOT NULL
);


CREATE TABLE IF NOT EXISTS logs (
    id INT AUTO_INCREMENT PRIMARY KEY,
    event VARCHAR(255) NOT NULL,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
);


-- Disable safe update mode for this session
SET SQL_SAFE_UPDATES = 0;

-- Now run your update (example: updating preferences)
UPDATE user_preferences
SET value = CASE key_name
    WHEN 'tts_voice' THEN 'en-US-JennyNeural'
    WHEN 'wakeword' THEN 'hey wiki'
    WHEN 'default_pasta_time' THEN '10'
    WHEN 'default_egg_time' THEN '7'
    WHEN 'default_rice_time' THEN '20'
    WHEN 'default_curry_time' THEN '25'
    WHEN 'default_study_time' THEN '25'
END
WHERE key_name IN ('tts_voice','wakeword','default_pasta_time','default_egg_time','default_rice_time','default_curry_time','default_study_time');

-- Re-enable safe updates
SET SQL_SAFE_UPDATES = 1;
