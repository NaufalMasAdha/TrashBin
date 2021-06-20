import folium


m = folium.Map(location=[5.550853653448776, 95.34531051279963],
    zoom_start=15, width=720, height=500)


tooltip= 'Lokasi Tempat Sampah'

folium.Marker([5.546920125071173, 95.34615322879506],
    icon=folium.Icon(icon='trash', color='green'),
    tooltip=tooltip).add_to(m),

folium.Marker([5.5531674813876775, 95.34132940619023],
    icon=folium.Icon(icon='trash', color='green'),
    tooltip=tooltip).add_to(m),

folium.Marker([5.549349660426704, 95.35001809873748],
    icon=folium.Icon(icon='trash', color='green'),
    tooltip=tooltip).add_to(m),

folium.Marker([5.54807704794343, 95.35658547167121],
    icon=folium.Icon(icon='trash', color='green'),
    tooltip=tooltip).add_to(m),

folium.Marker([5.545589661046841, 95.35045398634327],
    icon=folium.Icon(icon='trash', color='green'),
    tooltip=tooltip).add_to(m),

folium.Marker([5.549854351436044, 95.3527640573732],
    icon=folium.Icon(icon='trash', color='green'),
    tooltip=tooltip).add_to(m),

folium.Marker([5.550416441205517, 95.34409290075908],
    icon=folium.Icon(icon='trash', color='green'),
    tooltip=tooltip).add_to(m),



m.save('keterangan/Ulee_Kareng.html')
