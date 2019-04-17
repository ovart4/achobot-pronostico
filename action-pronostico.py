#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from hermes_python.hermes import Hermes

MQTT_IP_ADDR = "localhost"
MQTT_PORT = 1883
MQTT_ADDR = "{}:{}".format(MQTT_IP_ADDR, str(MQTT_PORT))


def intent_received(hermes, intent_message):

    if intent_message.intent.intent_name == 'josenka:Suma':
        sentence = 'La suma de'
    else:
        return
    
    primer = intent_message.slots.firstTerm.first().value
    segundo = intent_message.slots.secondTerm.first().value
    suma = primer + segundo
    
    entero1 = int(primer)
    entero2 = int(segundo)
    entero3 = int(suma)
    
    sentence += " : {}".format(str(entero1))
    sentence += " y : {}".format(str(entero2))
    sentence += " es : {}".format(str(entero3))
    
    
    
    hermes.publish_end_session(intent_message.session_id, sentence)


with Hermes(MQTT_ADDR) as h:
h.subscribe_intents(intent_received).start()
