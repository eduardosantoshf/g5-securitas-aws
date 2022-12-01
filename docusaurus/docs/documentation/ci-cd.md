---
sidebar_position: 1
---

# CI/CD

## Testing

To implement correctly DevOps practices and methodologies, we developed multiple workflows on the GitHub platform. Each one of this workflows is specific to a microservice, separating its CI/CD logic and properties.

Taking as an example the Human Detection service and looking at the `human-detection.yaml` file, we have on the sonar job, the following step:

~~~yaml
- name: Install tox and any other packages
    run: pip install tox
- name: Run tox
    run: tox -e py
~~~

On this step, we use the  Tox tool, a python test wrapper which allows us to configure the tests made by the [pytest](https://docs.pytest.org/en/7.1.x/) testing tool. This tool integrated with SonarCloud scan gives us the code coverage of the service.

## Code Coverage

Using the [SonarCloud](https://www.sonarsource.com/products/sonarcloud/) code coverage service, we can see the % of code which is covered by test, plus checking bugs and security vulnerabilities, code smells, etc. 

~~~yaml
 - name: SonarCloud Scan
    uses: SonarSource/sonarcloud-github-action@master
    env:
        GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}  # needed to get PR information, if any
        SONAR_TOKEN: ${{ secrets.SONAR_TOKEN_HUMAN_DETECTION }}
    with:
        projectBaseDir: HumanDetection/
~~~

On the code portion above, the referred step performs the SonarCloud scan. It is worth to mention that, for the purpose of this project, we used a feature of SonarCloud called monorepo, this feature is used when we have the necessity to have multiple SonarCloud projects inside the same git repository. In our case, as we have a microservices architecture, this feature came in hand, because it allowed us to set a specific scan for each service, in its own programming language, frameworks, etc.

[TODO: meter exemplo da interface do sonarcloud após um scan]: #

Still using the Human Detection service, we can check the code coverage scan results, accessing this [link](https://sonarcloud.io/project/overview?id=es-project-human-detection).