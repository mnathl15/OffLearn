
cd ng-rest && python api.py &  PIDIOS=$!
cd ng-web && npm start &  PIDMIX=$!
wait $PIDIOS
wait $PIDMIX
