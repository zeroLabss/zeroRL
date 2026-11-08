#!/bin/bash
set -e 

if [ -z "$1"]; then
	echo "No environment specified"
else
	ENV_BENCH=$1
fi

if [ -z "$2"]; then
	OUT_BENCH=""
else
	OUT_BENCH=$2
fi

if [ -z "$3"]; then
	DEVICE_BENCH="cpu"
else
	DEVICE_BENCH=$3
fi

for exp in {A..D}; do
        uv run scalability/run.py --experiment "$exp" --env "$ENV_BENCH" --out "$OUT_BENCH" --device "$DEVICE_BENCH"
done

uv run resource/run.py --env "$ENV_BENCH" --out "$OUT_BENCH" --device "$DEVICE_BENCH"
