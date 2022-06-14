package site.metacoding.weather.web;

import java.util.List;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;

import lombok.RequiredArgsConstructor;
import site.metacoding.weather.domain.Weather;
import site.metacoding.weather.domain.WeatherRepository;

@RequiredArgsConstructor
@Controller
public class WeatherController {

    private final WeatherRepository weatherRepository;
    
    @GetMapping("/weather")
    public String weather(Model model){
        List<Weather> weatherEntity = weatherRepository.findAll();
        model.addAttribute("weather", weatherEntity);
        return "/weather";
    }
}
