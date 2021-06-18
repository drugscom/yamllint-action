# yamllint action

Run yamllint.

## Inputs

### `config`

Custom configuration (as YAML source)

## Example usage

```yaml
uses: docker://ghcr.io/drugscom/yamllint-action:1
with:
  config:
    extends: default
    rules:
      document-start: disable
  args: |
    **/*.yml
    **/*.yaml
```
