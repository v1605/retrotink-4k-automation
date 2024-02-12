# retrotink-4k-automation

<img width="949" alt="exaple" src="https://github.com/v1605/retrotink-4k-automation/assets/55302877/0b77b89e-57a6-4474-906c-8b87c95264d3">

The purpose of this repository is to help users of the retrotink 4k automate changing profiles via home assistant and node-red. This is not a tutorial for node-red or homeassistant, so basic familiarity with thoses projects is required.
The examples are setup into 3 folders:
  1. esphome- this folder contains an example esphome config that using an [ir transmiter](https://esphome.io/components/remote_transmitter.html#remote-setting-up-infrared) to send remote commands to the retrotink.
  2. sdcardParsing- this contains a python script that can read the profiles folder of the retrotink and outputs a json object contains possitonal data on the profiles menu. This mapping is used to know how to navigate the profiles menu to select a specfic profile.
  3. nodered- contains an example node-red flow that selects a custom profile.
