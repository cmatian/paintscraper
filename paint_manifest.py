# The selenium driver won't click any elements. Use a manual url until Selenium click decides to work again.
data = {
    'green': 'https://www.games-workshop.com/en-US/detail?N=673862412&Ndi=3184893862&Ndn=GW_Painting_and_Modelling_Browse_Paint_by_Colour.dyn.dimensionPaintColour&Nr=AND%28sku.siteId%3AUS_gw%2Cproduct.locale%3Aen_US_gw%29&Nrs=collection%28%29%2Frecord%5Bproduct.startDate+%3C%3D+1590690120000+and+product.endDate+%3E%3D+1590690120000%5D',

    'brown': 'https://www.games-workshop.com/en-US/detail?N=2013579642&Ndi=3184893862&Ndn=GW_Painting_and_Modelling_Browse_Paint_by_Colour.dyn.dimensionPaintColour&Nr=AND%28sku.siteId%3AUS_gw%2Cproduct.locale%3Aen_US_gw%29&Nrs=collection%28%29%2Frecord%5Bproduct.startDate+%3C%3D+1590691800000+and+product.endDate+%3E%3D+1590691800000%5D',

    'blue': 'https://www.games-workshop.com/en-US/detail?N=2041751774&Ndi=3184893862&Ndn=GW_Painting_and_Modelling_Browse_Paint_by_Colour.dyn.dimensionPaintColour&Nr=AND%28sku.siteId%3AUS_gw%2Cproduct.locale%3Aen_US_gw%29&Nrs=collection%28%29%2Frecord%5Bproduct.startDate+%3C%3D+1590691800000+and+product.endDate+%3E%3D+1590691800000%5D',

    'grey': 'https://www.games-workshop.com/en-US/detail?N=2542067766&Ndi=3184893862&Ndn=GW_Painting_and_Modelling_Browse_Paint_by_Colour.dyn.dimensionPaintColour&Nr=AND%28sku.siteId%3AUS_gw%2Cproduct.locale%3Aen_US_gw%29&Nrs=collection%28%29%2Frecord%5Bproduct.startDate+%3C%3D+1590693180000+and+product.endDate+%3E%3D+1590693180000%5D',

    'flesh': 'https://www.games-workshop.com/en-US/detail?N=1417109135&Ndi=3184893862&Ndn=GW_Painting_and_Modelling_Browse_Paint_by_Colour.dyn.dimensionPaintColour&Nr=AND%28sku.siteId%3AUS_gw%2Cproduct.locale%3Aen_US_gw%29&Nrs=collection%28%29%2Frecord%5Bproduct.startDate+%3C%3D+1590693180000+and+product.endDate+%3E%3D+1590693180000%5D',

    'red': 'https://www.games-workshop.com/en-US/detail?N=531803153&Ndi=3184893862&Ndn=GW_Painting_and_Modelling_Browse_Paint_by_Colour.dyn.dimensionPaintColour&Nr=AND%28sku.siteId%3AUS_gw%2Cproduct.locale%3Aen_US_gw%29&Nrs=collection%28%29%2Frecord%5Bproduct.startDate+%3C%3D+1590693420000+and+product.endDate+%3E%3D+1590693420000%5D',

    'purple': 'https://www.games-workshop.com/en-US/detail?N=3396220678&Ndi=3184893862&Ndn=GW_Painting_and_Modelling_Browse_Paint_by_Colour.dyn.dimensionPaintColour&Nr=AND%28sku.siteId%3AUS_gw%2Cproduct.locale%3Aen_US_gw%29&Nrs=collection%28%29%2Frecord%5Bproduct.startDate+%3C%3D+1590693960000+and+product.endDate+%3E%3D+1590693960000%5D',

    'bone': 'https://www.games-workshop.com/en-US/detail?N=1367623709&Ndi=3184893862&Ndn=GW_Painting_and_Modelling_Browse_Paint_by_Colour.dyn.dimensionPaintColour&Nr=AND%28sku.siteId%3AUS_gw%2Cproduct.locale%3Aen_US_gw%29&Nrs=collection%28%29%2Frecord%5Bproduct.startDate+%3C%3D+1590693960000+and+product.endDate+%3E%3D+1590693960000%5D',

    'silver': 'https://www.games-workshop.com/en-US/detail?N=1134355817&Ndi=3184893862&Ndn=GW_Painting_and_Modelling_Browse_Paint_by_Colour.dyn.dimensionPaintColour&Nr=AND%28sku.siteId%3AUS_gw%2Cproduct.locale%3Aen_US_gw%29&Nrs=collection%28%29%2Frecord%5Bproduct.startDate+%3C%3D+1590694020000+and+product.endDate+%3E%3D+1590694020000%5D',

    'yellow': 'https://www.games-workshop.com/en-US/detail?N=3695711000&Ndi=3184893862&Ndn=GW_Painting_and_Modelling_Browse_Paint_by_Colour.dyn.dimensionPaintColour&Nr=AND%28sku.siteId%3AUS_gw%2Cproduct.locale%3Aen_US_gw%29&Nrs=collection%28%29%2Frecord%5Bproduct.startDate+%3C%3D+1590694020000+and+product.endDate+%3E%3D+1590694020000%5D',

    'gold': 'https://www.games-workshop.com/en-US/detail?N=2813407596&Ndi=3184893862&Ndn=GW_Painting_and_Modelling_Browse_Paint_by_Colour.dyn.dimensionPaintColour&Nr=AND%28sku.siteId%3AUS_gw%2Cproduct.locale%3Aen_US_gw%29&Nrs=collection%28%29%2Frecord%5Bproduct.startDate+%3C%3D+1590694020000+and+product.endDate+%3E%3D+1590694020000%5D',

    'orange': 'https://www.games-workshop.com/en-US/detail?N=4229952118&Ndi=3184893862&Ndn=GW_Painting_and_Modelling_Browse_Paint_by_Colour.dyn.dimensionPaintColour&Nr=AND%28sku.siteId%3AUS_gw%2Cproduct.locale%3Aen_US_gw%29&Nrs=collection%28%29%2Frecord%5Bproduct.startDate+%3C%3D+1590694020000+and+product.endDate+%3E%3D+1590694020000%5D',

    'white': 'https://www.games-workshop.com/en-US/detail?N=425682346&Ndi=3184893862&Ndn=GW_Painting_and_Modelling_Browse_Paint_by_Colour.dyn.dimensionPaintColour&Nr=AND%28sku.siteId%3AUS_gw%2Cproduct.locale%3Aen_US_gw%29&Nrs=collection%28%29%2Frecord%5Bproduct.startDate+%3C%3D+1590694080000+and+product.endDate+%3E%3D+1590694080000%5D',

    'pink': 'https://www.games-workshop.com/en-US/detail?N=659620007&Ndi=3184893862&Ndn=GW_Painting_and_Modelling_Browse_Paint_by_Colour.dyn.dimensionPaintColour&Nr=AND%28sku.siteId%3AUS_gw%2Cproduct.locale%3Aen_US_gw%29&Nrs=collection%28%29%2Frecord%5Bproduct.startDate+%3C%3D+1590694080000+and+product.endDate+%3E%3D+1590694080000%5D',

    'bronze': 'https://www.games-workshop.com/en-US/detail?N=93330276&Ndi=3184893862&Ndn=GW_Painting_and_Modelling_Browse_Paint_by_Colour.dyn.dimensionPaintColour&Nr=AND%28sku.siteId%3AUS_gw%2Cproduct.locale%3Aen_US_gw%29&Nrs=collection%28%29%2Frecord%5Bproduct.startDate+%3C%3D+1590694200000+and+product.endDate+%3E%3D+1590694200000%5D',

    'brass': 'https://www.games-workshop.com/en-US/detail?N=3078580043&Ndi=3184893862&Ndn=GW_Painting_and_Modelling_Browse_Paint_by_Colour.dyn.dimensionPaintColour&Nr=AND%28sku.siteId%3AUS_gw%2Cproduct.locale%3Aen_US_gw%29&Nrs=collection%28%29%2Frecord%5Bproduct.startDate+%3C%3D+1590694200000+and+product.endDate+%3E%3D+1590694200000%5D',

    'copper': 'https://www.games-workshop.com/en-US/detail?N=2590116596&Ndi=3184893862&Ndn=GW_Painting_and_Modelling_Browse_Paint_by_Colour.dyn.dimensionPaintColour&Nr=AND%28sku.siteId%3AUS_gw%2Cproduct.locale%3Aen_US_gw%29&Nrs=collection%28%29%2Frecord%5Bproduct.startDate+%3C%3D+1590694200000+and+product.endDate+%3E%3D+1590694200000%5D',

    'turquoise': 'https://www.games-workshop.com/en-US/detail?N=1906874889&Ndi=3184893862&Ndn=GW_Painting_and_Modelling_Browse_Paint_by_Colour.dyn.dimensionPaintColour&Nr=AND%28sku.siteId%3AUS_gw%2Cproduct.locale%3Aen_US_gw%29&Nrs=collection%28%29%2Frecord%5Bproduct.startDate+%3C%3D+1590694200000+and+product.endDate+%3E%3D+1590694200000%5D'
}
