# Bashate linter

Run bashate linter.

## Inputs

### `ignore`

Rules to ignore

### `error`

Rules to always error (rather than warn)

### `warn`

Rules to always warn (rather than error)

## Example usage

```yaml
uses: docker://ghcr.io/drugscom/bashate-action:1
with:
  ignore: E006
  args: '**/*.sh'
```
