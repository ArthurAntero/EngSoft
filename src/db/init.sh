#!/bin/bash

psql -U $POSTGRES_USER -d $POSTGRES_DB -a -f /tmp/schema.sql
psql -U $POSTGRES_USER -d $POSTGRES_DB -a -f /tmp/seeds.sql
