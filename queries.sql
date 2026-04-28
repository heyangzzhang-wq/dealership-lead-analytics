-- Dealership Lead Source Analytics Project

-- 1. Total leads by source
SELECT lead_source,
       COUNT(*) AS total_leads
FROM public.leads
GROUP BY lead_source
ORDER BY total_leads DESC;

-- 2. Sold deals by source
SELECT lead_source,
       COUNT(*) AS sold_deals
FROM public.leads
WHERE outcome ILIKE '%sold%'
GROUP BY lead_source
ORDER BY sold_deals DESC;

-- 3. Close rate by source
SELECT 
  lead_source,
  COUNT(*) AS total_leads,
  COUNT(*) FILTER (WHERE outcome ILIKE '%sold%') AS sold_deals,
  ROUND(
    100.0 * COUNT(*) FILTER (WHERE outcome ILIKE '%sold%') / COUNT(*),
    2
  ) AS close_rate_percent
FROM public.leads
GROUP BY lead_source
ORDER BY close_rate_percent DESC;

-- 4. Payment type among sold deals
SELECT payment_type,
       COUNT(*) AS deals
FROM public.leads
WHERE outcome ILIKE '%sold%'
GROUP BY payment_type
ORDER BY deals DESC;

-- 5. Monthly trend
SELECT month,
       COUNT(*) AS total_leads,
       COUNT(*) FILTER (WHERE outcome ILIKE '%sold%') AS sold_deals
FROM public.leads
GROUP BY month
ORDER BY month;
