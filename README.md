<p align="center">
    <img src="https://i.pinimg.com/originals/b8/c0/2e/b8c02ea45ceb70762691f01114323903.png" width="180" alt="Money With Wings">
</p>

<p align="center">
    <a href="https://drone.ppay.me/PicPay/picpay-dev-ms-withdraw"><img src="https://drone.ppay.me/api/badges/PicPay/picpay-dev-ms-withdraw/status.svg" alt="Build Status"></a>
    <a href="https://codebuild.us-east-1.amazonaws.com/badges?uuid=eyJlbmNyeXB0ZWREYXRhIjoiSlRuZlVsL0NzdDR6dWVDK1RXYmtocDNMVU42ZnM2dnNHbmdoNkVxOE9YQ25JL0FOTEJ4ZXRxOFF2ek1tNFNBOTF1TjlCcyt0UEFYbXJzMDUzVmpOSjBrPSIsIml2UGFyYW1ldGVyU3BlYyI6Ilp5ZFpOSGtEYmJ5SjlnT3MiLCJtYXRlcmlhbFNldFNlcmlhbCI6MX0%3D&branch=master"><img src="https://codebuild.us-east-1.amazonaws.com/badges?uuid=eyJlbmNyeXB0ZWREYXRhIjoiSlRuZlVsL0NzdDR6dWVDK1RXYmtocDNMVU42ZnM2dnNHbmdoNkVxOE9YQ25JL0FOTEJ4ZXRxOFF2ek1tNFNBOTF1TjlCcyt0UEFYbXJzMDUzVmpOSjBrPSIsIml2UGFyYW1ldGVyU3BlYyI6Ilp5ZFpOSGtEYmJ5SjlnT3MiLCJtYXRlcmlhbFNldFNlcmlhbCI6MX0%3D&branch=master" alt="AWS CodeBuild"></a>
    <a href="https://app.codacy.com/gh/PicPay/picpay-dev-ms-withdraw/dashboard"><img src="https://api.codacy.com/project/badge/Grade/5e7e761440704bca86f0fc58f227e942" alt="Code Quality"></a>
    <a href="https://app.codacy.com/gh/PicPay/picpay-dev-ms-withdraw/files"><img src="https://api.codacy.com/project/badge/Coverage/5e7e761440704bca86f0fc58f227e942" alt="Coverage"></a>
</p>

## About
Withdraw funds from PicPay. 

## Running the project

### Dependencies
- [GitHub Token](https://github.com/settings/tokens)
- [Docker Login](https://picpay.atlassian.net/wiki/spaces/TechTeam/pages/460587015/Como+usar+imagem+docker+localmente)

### External Services

Dependencies that you should run to make this project work properly.

#### Microservices

| Name                                                                               | Description                                                          | Required for App |
|------------------------------------------------------------------------------------|----------------------------------------------------------------------|------------------|
| [Legacy](https://github.com/PicPay/picpay-dev-ms-legacy)                           | To create movement and cnab                                          |                  |
| [Consumer](https://github.com/PicPay/picpay-dev-ms-consumer)                       | Get details about a consumer                                         |                  |
| [Gateway](https://github.com/PicPay/picpay-dev-ms-gateway)                         | Web requests gateway                                                 | YES              |
| [Authorization](https://github.com/PicPay/picpay-dev-ms-authorization)             | Authentication application                                           | YES              |
| [Feed](https://github.com/PicPay/picpay-dev-ms-feed)                               | Show withdraw's feed items                                           | YES              |
| [Notification](https://github.com/PicPay/picpay-dev-ms-notification)               | Alert consumer regarding a withdraw update                           | YES              |
| [Cashout-24Horas](https://github.com/PicPay/picpay-dev-ms-cashout-24horas)         | Get available withdraw methods                                       | YES              |
| [Digital Account](https://github.com/PicPay/picpay-dev-ms-digital-account)         | Get details about a consumer account                                 |                  |
| [MML](https://github.com/PicPay/picpay-dev-ms-mml)                                 | Communicate with Nexxera and Neogrid in order to exchange cnab files |                  |
| [Electronic Transfer](https://github.com/PicPay/picpay-dev-ms-electronic-transfer) | Make transfers with Open Banking APIs such as Stone and Original     |                  |
| [BaaS Wire Transfer](https://github.com/PicPay/baas-wire-transfer)                 | Make transfers with SPB                                              |                  |

#### Databases

| Name                                                     | Table                  | Description                           |
|----------------------------------------------------------|------------------------|---------------------------------------|
| [Legacy](https://github.com/PicPay/picpay-dev-ms-legacy) | bank_accounts          | Get details of a bank account         |
| [Legacy](https://github.com/PicPay/picpay-dev-ms-legacy) | bancos                 | Get bank information                  |
| [Legacy](https://github.com/PicPay/picpay-dev-ms-legacy) | general_parameters     | Get general application settings      |
| [Legacy](https://github.com/PicPay/picpay-dev-ms-legacy) | consumer_under_reviews | Check if consumer is under review     |

### 1. Make a copy of .env.example
```bash
cp .env.example .env
```

### 2. Export the following variable
```bash
export COMPOSER_AUTH='{"github-oauth": {"github.com": "<github_token>"}}'
```

### 3. Run these command to up the container and install composer packages
```bash
docker-compose up -d
docker exec -it api.withdraw.dev composer install
```

### 4. Run migrations
```bash
docker-compose exec api.withdraw.dev php artisan migrate
```

### 5. Run seeders
```bash
docker-compose exec api.withdraw.dev php artisan db:seed
```

## PHPUnit
```bash
docker exec -it api.withdraw.dev ./vendor/bin/phpunit
```

## PHP_CodeSniffer

### Looking for errors
```bash
docker exec -it api.withdraw.dev ./vendor/bin/phpcs --standard=phpcs.xml -sp app bootstrap config database routes tests
```

### Fixing errors
```bash
docker exec -it api.withdraw.dev ./vendor/bin/phpcbf --standard=phpcs.xml app bootstrap config database routes tests
```

## Documentation
- [Business Docs](https://picpay.atlassian.net/wiki/spaces/CO/pages/857211350/MS+Withdraw)
- [API Docs](http://localhost:32789) - _You must run the project to look at it._

## Monitoring

Services we have integrated to check the application's health.

| Name           | Environment                                                                                                                                             | 
|----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------|
| New Relic APM  | [Production](https://rpm.newrelic.com/accounts/2407767/applications/572590086) ¦ [QA](https://rpm.newrelic.com/accounts/2720018/applications/544355946) | 
| New Relic Logs | [Production](https://bit.ly/3gffyei) ¦ [QA](https://bit.ly/3iZlmKV)                                                                                     | 
| Slack          | [Production](https://picpay.slack.com/archives/C015JHQDC48) ¦ [QA](https://picpay.slack.com/archives/C0150QKBE20)                                       | 
| Sentry         | [Production](http://sentry.ppay.me/sentry/withdraw/?environment=prod) ¦ [QA](http://sentry.ppay.me/sentry/withdraw/?environment=qa)                     | 

_If you don't have access to one of the services listed above ask on [#acessos](https://picpay.slack.com/archives/CR33W9JSC) channel._

## Workflow
As several teams may work in this repository the development and deployment workflow is a little tricky. You can find all this process defined in the [CONTRIBUTING](./CONTRIBUTING.md) guide.
