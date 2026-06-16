def count(id_xe, diem_hien_tai, diem_cu, lan_duong, in_counts, out_counts, danh_sach, frame_hien_tai, chieu_cao_box_hien_tai):
    cx, cy = diem_hien_tai
    for i, lan in enumerate(lan_duong):
        if cv2.pointPolygonTest(lan, diem_hien_tai, False) >= 0:
            cy_hien_tai = diem_hien_tai[1]
            cy_cu = diem_cu[1]

            if cy_hien_tai != cy_cu:
                is_ghost = False
                for old_id, (old_cx, old_cy, old_height, old_frame) in vi_tri_xe_da_dem.items():
                    frame_lech = frame_hien_tai - old_frame
                    
                    if frame_lech < 20: 
                        khoang_cach = np.sqrt((cx - old_cx)**2 + (cy - old_cy)**2)
                        ban_kinh_bat_ma = max(30, min(old_height * 0.5, 70))
                        
                        if khoang_cach < ban_kinh_bat_ma:
                            is_ghost = True 
                            break

                if not is_ghost:
                    if cy_hien_tai > cy_cu:
                        in_counts[i] += 1
                    elif cy_hien_tai < cy_cu:
                        out_counts[i] += 1

                    vi_tri_xe_da_dem[id_xe] = (cx, cy, chieu_cao_box_hien_tai, frame_hien_tai)

                danh_sach.add(id_xe)
            break