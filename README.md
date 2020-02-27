# PollyTTS
AWS Polly TTS for Kalliope

## Installation
```bash
kalliope install --git-url https://github.com/corus87/kalliope_pollytts.git
```

## Parameters

| parameter             | required | type   | default    | Comment |
|-----------------------|----------|--------|------------|---------|
| voice                 | No       | string | Ivy        | [Voicelist](https://docs.aws.amazon.com/polly/latest/dg/voicelist.html) |
| aws_access_key_id     | Yes      | string  | None      | [Get AWS keys](https://docs.aws.amazon.com/ses/latest/DeveloperGuide/get-aws-keys.html) |
| aws_secret_access_key | Yes      | string  | None      | [Get AWS keys](https://docs.aws.amazon.com/ses/latest/DeveloperGuide/get-aws-keys.html) |
| region_name           | No       | string  | eu-west-2 | [Regions](https://docs.aws.amazon.com/de_de/general/latest/gr/rande.html) |

## Example settings

```
default_text_to_speech: "pollytts"
cache_path: "/tmp/kalliope_tts_cache"

text_to_speech:
  - pollytts:
     voice: "Vicki"
     aws_access_key_id: "ABCDEF12345GHIJKL678"
     aws_secret_access_key: "ABCDefgh12345ijklmn+o6789PqrstUVWXYZ0"
     region_name: "eu-central-1"
```


## Note

You have to add the path in your settings.yml to the tts folder in your starter.
```
# ---------------------------
# resource directory path
# ---------------------------
resource_directory:
  tts: "resources/tts"
```
