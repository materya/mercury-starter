<h1 align="center">
  <img src="doc/assets/mercury_materya_starter_logo.png" alt="Mercury Materya Starter Kit" />
</h1>

[![License][license-image]][license-url]

A starter to use the [mercury library](https://github.com/materya/mercury) for quantitative trading.

This is a base example and is not meant to be ready out of the box.

A container environment is available to run the trading engine, you can also use the [VSCode Development Container](https://code.visualstudio.com/docs/remote/containers) feature.

## Quick start

1. Clone this repo, you know the drill
2. Take a look at [main.py](main.py) for a basic setup of the mercury engine and tweak as you like. You need at least a stragegy and a broker.
3. You can use the [config.cfg](config.cfg) example to configure your engine. In a production context it is strongly advised to use either environment variables, kubernetes secrets or any kind of vault/protection on sensible parameters.
4. You can start the engine with a `make run` either locally or in the container, the `Makefile` will detect the context and ensure to run in the container.

## Local setup

If you want to use this starter locally, ensure you have properly setup your environment with python `>= 3.6` (with [virtualenv](https://github.com/pypa/virtualenv) or else) and run `make install` first.

## License

[GPL-3.0](LICENSE)

[license-image]: https://img.shields.io/github/license/materya/mercury-starter?style=flat-square
[license-url]: LICENSE
