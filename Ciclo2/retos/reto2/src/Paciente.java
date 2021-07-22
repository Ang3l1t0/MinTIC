public class Paciente {

    public String diagnosticar(String nauseas, String vomitos, String dolorAbdominal, String diarrea,
            String fiebre) {
        String enfermedad;

        // Validaciones de enfermedad
        if (nauseas.equals("si") && vomitos.equals("si") && dolorAbdominal.equals("si") && diarrea.equals("si")
                && fiebre.equals("si")) {
            enfermedad = "Staphylococcus aureus";
        } else if (nauseas.equals("si") && vomitos.equals("si") && dolorAbdominal.equals("no") && diarrea.equals("si")
                && fiebre.equals("si")) {
            enfermedad = "Norovirus";
        } else if (nauseas.equals("si") && vomitos.equals("si") && dolorAbdominal.equals("no") && diarrea.equals("no")
                && fiebre.equals("no")) {
            enfermedad = "Bacillus cereus";
        } else if (nauseas.equals("no") && vomitos.equals("no") && dolorAbdominal.equals("si") && diarrea.equals("no")
                && fiebre.equals("si")) {
            enfermedad = "Taenia saginata";
        } else if (nauseas.equals("no") && vomitos.equals("si") && dolorAbdominal.equals("no") && diarrea.equals("si")
                && fiebre.equals("no")) {
            enfermedad = "Rotavirus";
        } else {
            enfermedad = "Sin diagnostico";
        }
        return enfermedad;
    }
}