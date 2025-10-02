CREATE MIGRATION m1eyftlvuty4qozw6itzxo4x7as7fyztpcioaejj2wdyzngy6qbgfa
    ONTO m1xg2zzuvmz6bo6cipehfydub7ixfnlncaeucgnizsq7odrfybc6oa
{
  ALTER TYPE default::Movie {
      CREATE INDEX ON (.title);
  };
};
