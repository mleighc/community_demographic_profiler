# Data Source: https://overpass-turbo.eu/
# OpenStreetMap data via Overpass Turbo

"""
## 🍽️ Calculating Restaurants Per Capita by County

This workflow outlines how to calculate **restaurants per capita** by U.S. county using a combination of **open location data** and **Census population data**.

---

### 🧪 Formula
```text
Restaurants per capita = (# of restaurants in area) / (population in area)
```

Scale it for comparison:
```text
Restaurants per 10,000 people = (restaurants / population) * 10,000
```

---

## ✅ Step-by-Step Workflow

### 🔍 Step 1: Count of Restaurants per County

#### Option A: OpenStreetMap (Overpass API)
- Query all nodes with `amenity=restaurant` within a county polygon
- Use [Overpass Turbo](https://overpass-turbo.eu) or Python (`overpy`, `osmnx`)

**Sample Overpass Query (Wayne County, MI):**
```ql
[out:json][timeout:25];
area["name"="Wayne County"]["admin_level"="6"];
(
  node["amenity"="restaurant"](area);
);
out count;
```

**Sample Output (Nodes Only):**
```json
"tags": {
  "nodes": "798",
  "ways": "0",
  "relations": "0",
  "areas": "0",
  "total": "798"
}
```

**Expanded Query (Nodes + Ways):**
```ql
[out:json][timeout:25];
area["name"="Wayne County"]["admin_level"="6"]->.searchArea;
(
  node["amenity"="restaurant"](area.searchArea);
  way["amenity"="restaurant"](area.searchArea);
  relation["amenity"="restaurant"](area.searchArea);
);
out count;
```

**Sample Output (Nodes + Ways):**
```json
"tags": {
  "nodes": "798",
  "ways": "460",
  "relations": "0",
  "areas": "0",
  "total": "1258"
}
```

✅ Free and open
⚠️ Coverage varies depending on OSM completeness

---

#### Option B: Google Places API or Yelp API
- Use bounding boxes or place search by county
- Requires API key and daily quota management

---

### 🔍 Step 2: Get County Population
Use ACS 5-Year Estimates:
- Variable `B01003_001E`: Total population

If already in DataFrame:
```python
population = df["total_population"]
```

---

### 🔍 Step 3: Merge & Calculate
Assuming:
- `df_counts`: has `county_fips`, `restaurant_count`
- `df_pop`: has `county_fips`, `total_population`

```python
df = df_counts.merge(df_pop, on="county_fips")
df["restaurants_per_10k"] = (df["restaurant_count"] / df["total_population"]) * 10000
```

---

## 🚀 Optional Enhancements
- **Normalize**: Compare to national/state median
- **Categorize**: Count by type (e.g., fast food vs. dine-in)
- **Visualize**: Create choropleth maps or bar charts using Altair, Quarto, or Plotly

---

## 🛠️ Next Steps
- Script Overpass API pulls for a few Southeast MI counties
- Join with ACS population data
- Visualize and interpret!

"""
