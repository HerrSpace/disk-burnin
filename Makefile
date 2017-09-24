.PHONY: vcr-bin-teardown vcr-bin-setup vcr-record-setup vcr-replay-setup test
export

# Fabric won't do double ssh proxy jumps..
VCR_REMOTE_HOST=root@localhost:2223
VCR_DATA_DIR=./test/vcr-data/
VCR_BIN_DIR=./test/vcr-bin/
VCR_PATH=$(VCR_BIN_DIR):$(PATH)

vcr-bin-teardown:
	rm -rf $(VCR_BIN_DIR)

vcr-bin-setup: vcr-bin-teardown
	$(eval PATH := $(VCR_PATH))
	mkdir $(VCR_BIN_DIR)
	ln -s ../../../shell-vcr/main.py $(VCR_BIN_DIR)/sas2ircu
	ln -s ../../../shell-vcr/main.py $(VCR_BIN_DIR)/camcontrol

vcr-record-setup: vcr-bin-setup
	$(eval VCR_MODE := RECORD)

vcr-replay-setup: vcr-bin-setup
	$(eval VCR_MODE := REPLAY)

test:
	python3 -m unittest discover

test-record: vcr-record-setup test vcr-bin-teardown

test-replay: vcr-replay-setup test vcr-bin-teardown

run:
	python3 main.py

run-record: vcr-record-setup run vcr-bin-teardown

run-replay: vcr-replay-setup run vcr-bin-teardown
