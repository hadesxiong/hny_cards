from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "hny_dict_main" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "dict_id" VARCHAR(64) NOT NULL UNIQUE,
    "dict_index" VARCHAR(128) NOT NULL,
    "dict_code" INT NOT NULL  DEFAULT 1,
    "dict_value" VARCHAR(128) NOT NULL,
    "dict_name" VARCHAR(128) NOT NULL,
    "dict_statu" INT NOT NULL  DEFAULT 1,
    "dict_create_dt" TIMESTAMPTZ   DEFAULT CURRENT_TIMESTAMP,
    "dict_update_dt" TIMESTAMPTZ   DEFAULT CURRENT_TIMESTAMP,
    "dict_create_usr" VARCHAR(64) NOT NULL,
    "dict_update_usr" VARCHAR(64) NOT NULL,
    "dict_ext" JSONB,
    CONSTRAINT "uid_hny_dict_ma_dict_in_28309f" UNIQUE ("dict_index", "dict_code", "dict_name")
);
CREATE TABLE IF NOT EXISTS "hny_action_main" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "action_id" VARCHAR(64) NOT NULL UNIQUE,
    "action_type" INT NOT NULL  DEFAULT 1,
    "action_target" VARCHAR(128) NOT NULL  DEFAULT 'homepage',
    "action_by" VARCHAR(128) NOT NULL,
    "action_create_dt" TIMESTAMPTZ,
    "action_ext" JSONB
);
CREATE TABLE IF NOT EXISTS "hny_qian_main" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "qian_id" VARCHAR(64) NOT NULL UNIQUE,
    "qian_number" INT NOT NULL  DEFAULT 0,
    "qian_create_by" VARCHAR(64) NOT NULL,
    "qian_create_dt" TIMESTAMPTZ,
    "qian_ext" JSONB
);
CREATE TABLE IF NOT EXISTS "hny_guest_main" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "guest_id" VARCHAR(64) NOT NULL UNIQUE,
    "guest_finger" VARCHAR(128) NOT NULL UNIQUE,
    "guest_create_dt" TIMESTAMPTZ,
    "guest_ext" JSONB
);
CREATE TABLE IF NOT EXISTS "hny_user_info" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "usr_id" VARCHAR(64) NOT NULL UNIQUE,
    "usr_nick" VARCHAR(128) NOT NULL,
    "usr_avatar" VARCHAR(512),
    "guest_id" VARCHAR(64) NOT NULL UNIQUE,
    "info_create_dt" TIMESTAMPTZ,
    "info_update_dt" TIMESTAMPTZ,
    "info_ext" JSONB
);
CREATE TABLE IF NOT EXISTS "hny_user_main" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "usr_id" VARCHAR(64) NOT NULL UNIQUE,
    "usr_type" INT NOT NULL  DEFAULT 1,
    "usr_class" INT NOT NULL  DEFAULT 1,
    "usr_create_dt" TIMESTAMPTZ,
    "usr_update_dt" TIMESTAMPTZ,
    "usr_ext" JSONB
);
CREATE TABLE IF NOT EXISTS "aerich" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "version" VARCHAR(255) NOT NULL,
    "app" VARCHAR(100) NOT NULL,
    "content" JSONB NOT NULL
);"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        """
