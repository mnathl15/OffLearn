
cd ng-rest && python api.py &  PIDIOS=$!
cd ng_web && npm start &  PIDMIX=$!
wait $PIDIOS
wait $PIDMIX
