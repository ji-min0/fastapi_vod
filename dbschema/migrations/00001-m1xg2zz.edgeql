CREATE MIGRATION m1xg2zzuvmz6bo6cipehfydub7ixfnlncaeucgnizsq7odrfybc6oa
    ONTO initial
{
  CREATE FUTURE simple_scoping;
  CREATE TYPE default::Person {
      CREATE REQUIRED PROPERTY name: std::str;
  };
  CREATE TYPE default::Movie {
      CREATE MULTI LINK actors: default::Person;
      CREATE PROPERTY title: std::str;
  };
};
