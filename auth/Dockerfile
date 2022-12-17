FROM quay.io/keycloak/keycloak:latest as builder

# Enable health and metrics support
ENV KC_HEALTH_ENABLED=true
ENV KC_METRICS_ENABLED=true

WORKDIR /opt/keycloak
RUN /opt/keycloak/bin/kc.sh build --features=preview,scripts

FROM quay.io/keycloak/keycloak:latest
COPY --from=builder /opt/keycloak/ /opt/keycloak/
COPY realm-export-aws.json /opt/keycloak/data/import/

# change these values to point to a running postgres instance
ENV KEYCLOAK_ADMIN=kc_admin
ENV KEYCLOAK_ADMIN_PASSWORD=kc_admin_pass

ENTRYPOINT ["/opt/keycloak/bin/kc.sh", "start-dev"]
