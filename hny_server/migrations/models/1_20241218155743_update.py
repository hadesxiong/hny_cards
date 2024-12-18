from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "hny_qian_main" ADD "qian_type" VARCHAR(32) NOT NULL;
        ALTER TABLE "hny_qian_main" ADD "qian_tiangan" VARCHAR(32) NOT NULL;
        ALTER TABLE "hny_qian_main" ADD "qian_sentence" VARCHAR(128) NOT NULL;
        ALTER TABLE "hny_qian_main" DROP COLUMN "qian_create_dt";
        ALTER TABLE "hny_qian_main" DROP COLUMN "qian_create_by";
        ALTER TABLE "hny_qian_main" ALTER COLUMN "qian_number" SET DEFAULT 1;
        CREATE TABLE IF NOT EXISTS "hny_qian_record" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "record_id" VARCHAR(64) NOT NULL UNIQUE,
    "qian_number" INT NOT NULL  DEFAULT 0,
    "record_create_by" VARCHAR(64) NOT NULL,
    "record_create_dt" TIMESTAMPTZ,
    "record_ext" JSONB
);"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "hny_qian_main" ADD "qian_create_dt" TIMESTAMPTZ;
        ALTER TABLE "hny_qian_main" ADD "qian_create_by" VARCHAR(64) NOT NULL;
        ALTER TABLE "hny_qian_main" DROP COLUMN "qian_type";
        ALTER TABLE "hny_qian_main" DROP COLUMN "qian_tiangan";
        ALTER TABLE "hny_qian_main" DROP COLUMN "qian_sentence";
        ALTER TABLE "hny_qian_main" ALTER COLUMN "qian_number" SET DEFAULT 0;
        DROP TABLE IF EXISTS "hny_qian_record";"""
