CREATE MIGRATION m1l7fq2lttzvjjxazpop4ip6jyk54fspxkaf33rn6yxu22ylm2lslq
    ONTO m1lthkyhknep6ewo6s3lhvy6jmxi6i6mtu3bhvrmuwtfnrr4yzecmq
{
  ALTER TYPE default::Meeting {
      CREATE PROPERTY end_date: std::cal::local_date;
      CREATE REQUIRED PROPERTY location: std::str {
          SET default := '';
      };
      CREATE PROPERTY start_date: std::cal::local_date;
      CREATE REQUIRED PROPERTY title: std::str {
          SET default := '';
      };
  };
};
