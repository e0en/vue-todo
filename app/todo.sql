CREATE TABLE IF NOT EXISTS "todos" (
    "uuid" VARCHAR(36) NOT NULL PRIMARY KEY,
    "content" TEXT,
    "is_done" BOOLEAN NOT NULL DEFAULT 0,
    "time_create" DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "time_edit" DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS "users" (
    "email" TEXT NOT NULL PRIMARY KEY,
    "pw_hash" TEXT NOT NULL
);
